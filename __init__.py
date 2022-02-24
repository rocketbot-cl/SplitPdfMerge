# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import os
import glob

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'SplitPdfMerge' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path = [cur_path] + sys.path
    


from PyPDF2 import PdfFileReader, PdfFileWriter
global txt

def reset_eof_of_pdf_return_stream(pdf_stream_in:list):
    # find the line position of the EOF
    for i, x in enumerate(txt[::-1]):
        if b'%%EOF' in x:
            actual_line = len(pdf_stream_in)-i
            print(f'EOF found at line position {-i} = actual {actual_line}, with value {x}')
            break

    # return the list up to that point
    return pdf_stream_in[:actual_line]

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "split_pdf":
    path = GetParams("pdf").replace("/", os.sep)
    folder = GetParams("folder")
    step = GetParams("step") or 1
    step = int(step)

    r = True
    try:
        fname = os.path.splitext(os.path.basename(path))[0]
        pdf = PdfFileReader(path)
        page_number = pdf.getNumPages()
        start = 0
        while start < page_number:
            end = start + step
            if end > page_number:
                end = page_number
            pdf_writer = PdfFileWriter()
            for page in range(start, end):
                pdf_writer.addPage(pdf.getPage(page))
            output_filename = '{}_page_{}.pdf'.format(fname, start + 1)
            start = end
            with open(folder + os.sep + output_filename, 'wb') as out:
                pdf_writer.write(out)
                print('Created: {}'.format(output_filename))
    except Exception as e:
        raise Exception(e)

if module == "merge_pdf":

    input_ = GetParams("pdfs_folder")
    output = GetParams("output_folder")

    output += ".pdf"
    pdf_writer = PdfFileWriter()
    pdfs = glob.glob(input_ + os.sep + "*.pdf")
    pdfs.sort()

    for pdf in pdfs:

        pdf = pdf.replace("\\", "/")

        with open(pdf, 'rb') as p:
            txt = (p.readlines())

        txtx = reset_eof_of_pdf_return_stream(txt)

        with open(pdf, 'wb') as f:
            f.writelines(txtx)
        pdf_reader = PdfFileReader(pdf, strict=False)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output, 'wb') as fh:
            pdf_writer.write(fh)

if module == "encrypt_pdf":
    path = GetParams("path")
    out = GetParams("out")
    password = GetParams("pass")

    try:
        with open(path, "rb") as pdf:
            input_pdf = PdfFileReader(pdf)

            output = PdfFileWriter()
            output.appendPagesFromReader(input_pdf)
            output.encrypt(password)

            with open(out, "wb") as out_pdf:
                output.write(out_pdf)

    except Exception as e:
        PrintException()
        raise e

if module == "read_pdf":
    path = GetParams("path")
    password = GetParams("pass")
    result = GetParams("result")

    try:
        text = ""
        with open(path, "rb") as pdf:
            reader = PdfFileReader(pdf)

            if reader.isEncrypted:
                reader.decrypt(password)

            page_number = reader.numPages

            for i in range(page_number):
                page = reader.getPage(i)
                text += page.extractText()

        SetVar(result, text)
    except Exception as e:
        PrintException()
        raise e

if module == "decrypt_pdf":

    in_path = GetParams("in_path")
    pass_pdf = GetParams("pass_pdf")
    out_path = GetParams("out_path")

    try:
        try:
            out = PdfFileWriter()
            file = PdfFileReader(in_path, password=pass_pdf)
            if file.isEncrypted:

                file.decrypt('')
                for idx in range(file.numPages):
                    page = file.getPage(idx)
                    out.addPage(page)

                with open(out_path, "wb") as f:
                    out.write(f)

                print("File decrypted Successfully.")
            else:
                print("File already decrypted.")
        except:
            import subprocess
            FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
            bin_path = cur_path + os.sep + "bin_qpdf" + os.sep + "qpdf"
            args = bin_path  + " --decrypt --password={pass_pdf} {in_path} {out_path} ".format(pass_pdf=pass_pdf, in_path=in_path, out_path=out_path)
            subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)


    except Exception as e:
        PrintException()
        raise e

if (module == "SplitPdfMergeSpecificStep"):
    path = GetParams("pdf").replace("/", os.sep)
    folder = GetParams("folder")
    step = GetParams("step")
    step = eval(step)
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    page_number = pdf.getNumPages()

    try:
        for each in step:

            realStep = each.split("-")
            pdf_writer = PdfFileWriter()

            for page in range((int(realStep[0])) - 1, int(realStep[1])):
                pdf_writer.addPage(pdf.getPage(page))
                output_filename = '{}_page_{}.pdf'.format(fname, f"{realStep[0]}-{realStep[1]}")

            with open(folder + os.sep + output_filename, 'wb') as out:
                pdf_writer.write(out)
                print('Created: {}'.format(output_filename))

    except Exception as e:
        PrintException()
        raise e