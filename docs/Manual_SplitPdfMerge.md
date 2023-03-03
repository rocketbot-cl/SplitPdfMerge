# SplitPdfMerge
  
Module for performing actions with PDF files such as splitting and merging files    

*Read this in other languages: [English](Manual_SplitPdfMerge.md), [Español](Manual_SplitPdfMerge.es.md).*
  
![banner](imgs/Banner_SplitPdfMerge.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module
In order to use this module, you have to select the PDF/s to use and execute the functions.


## Description of the commands

### Split Pdf
  
Split PDF
|Parameters|Description|example|
| --- | --- | --- |
|Path to PDF|Path to PDF file that you want to divide.|C:/Users/User/Downloads/sample.pdf|
|Path and name of the folder where to save the pdf|Path to use for save the resulting PDFs.|C:/Users/User/Desktop/PDF |
|Every few pages divide|Number of pages in wich the pace will be set to divide the PDF.|1|

### Merge Pdf
  
Merge PDFs 
|Parameters|Description|example|
| --- | --- | --- |
|Folder path with pdfs|Path that contains all PDFs to combine.|C:/Users/User/Desktop/PDF|
|Path and name of the file where to save the pdf|Path to use for save the resulting PDF.|C:/Users/User/Desktop/PDF/merge.pdf|

### Encrypt Pdf
  
Add password to a PDF
|Parameters|Description|example|
| --- | --- | --- |
|PDF to encrypt|Path to the PDF that you want to encrypt.|C:/Users/User/Downloads/sample.pdf|
|Path and name of the file where to save the pdf|Path to use for save the resulting PDF.|C:/Users/User/Downloads/sample.pdf|
|Password|Password wanted to use in the encryption.|s3cr3t-p4ss|

### Read Encrypted Pdf
  
Read a pdf with password
|Parameters|Description|example|
| --- | --- | --- |
|Encrypted PDF|Path where the encrypted PDF is.|C:/Users/User/Downloads/sample.pdf|
|Password|Password to decrypt the PDF.|s3cr3t-p4ss|
|Result|Variable to save the result.|pdf_read|

### Decrypt Pdf
  
Decrypt PDF with a password
|Parameters|Description|example|
| --- | --- | --- |
|Encrypted PDF|Path where the encrypted PDF is.|C:/Users/User/Downloads/sample.pdf|
|Password|Password to decrypt the PDF.|s3cr3t-p4ss|
|Save decrypt PDF|Path to save the decrypted PDF.|C:/Users/User/Downloads/output.pdf|

### Split Pdf in specific steps
  
Splits the pdf in a certain pace
|Parameters|Description|example|
| --- | --- | --- |
|Path to PDF|Path to PDF file that you want to divide.|C:/Users/User/Downloads/sample.pdf|
|Path and name of the folder where to save the pdf|Path to use for save the resulting PDFs.|C:/Users/User/Desktop/PDF |
|How to divide the PDF|Steps in wich the PDF will be divided.|['1-3', 4-5']|
