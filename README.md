# Partsbox Label Generator
 PartDB-Like Label Generator for Partsbox

Requires reportlab, qrcode[pil], requests, pyPDF2

Your API key for partsbox should be placed in a file called "secrets.txt" with the format 'APIKey,xxx' where 'xxx' is your API key.

This is not meant to be a fully featured add-on to partsbox. This is a tool I am developing for myself to help me manage my inventory. I am not an active developer and this software wont work forever, but I figure it might help someone else if it helps me.

To use it, make sure you have all the dependencies installed, and add your partsbox API key to the secrets file. From there, run main.py and follow the prompts to generate labels for parts. The end result of this program will be a pdf file with one or more labels that you can print. I am using a Brother QL-570 printer with 29mm continuous tape.

The default label generated is a 73mm x 29mm label cut from the continuous tape. There are references to a "magazine" or "compact" label, which is 65mm x 29mm. These labels are designed to fit onto the back of 3D printed SMD tape magazines found here: https://www.thingiverse.com/thing:3952021   credit to Thingiverse user robin7331 for the component storage. 

![IMG_8892](https://github.com/user-attachments/assets/9d63a42c-bcc5-4e9c-be7e-1178ab766d79)
The label shown in this picture is old and not representative of the new template I am using, see below for what the new design is.

The template for labels is hardcoded to what works for me. You are welcome to clone this and add your own template. Some examples of the styles that I programmed are below.

For all styles, the QR code contains the part number.

This is a magazine label, 65x29. Two rows possible for the part number, description, and storage location. The footprint is limited to one line and will be truncated if longer.

![image](https://github.com/user-attachments/assets/d9606cb5-cb46-4bea-906d-1a9171f77a26)

This is a standard label, 73x29. It fits nicely on these 2"x3" bags I bought off eBay: https://www.ebay.com/itm/192383069329?var=493083455428
On the standard label you get one line for everything but the description, which has two lines. The max length for part number is about 30 characters and description about 82 characters.

![image](https://github.com/user-attachments/assets/32fc9a2c-1712-41d5-b93c-d52b1839ee6a)
