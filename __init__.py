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

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import glob

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "split_pdf":
    path = GetParams("pdf").replace("/", os.sep)
    folder = GetParams("folder")
    step = GetParams("step") or 1
    print(step)
    step = int(step)

    r = True
    try:
        fname = os.path.splitext(os.path.basename(path))[0]
        print(fname)
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

    input = GetParams("pdfs_folder")
    output = GetParams("output_folder")

    output += ".pdf"
    pdf_writer = PdfFileWriter()
    pdfs = glob.glob(input + os.sep + "*.pdf")
    pdfs.sort()
    print(pdfs)

    for pdf in pdfs:
        print(pdf)
        pdf_reader = PdfFileReader(pdf)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output, 'wb') as fh:
            pdf_writer.write(fh)
