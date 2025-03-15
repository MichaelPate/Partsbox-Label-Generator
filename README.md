# Partsbox Label Generator
 PartDB-Like Label Generator for Partsbox

Requires reportlab, qrcode[pil], requests

Your API key for partsbox should be placed in a file called "secrets.txt" with the format 'APIKey,xxx' where 'xxx' is your API key.

This is not meant to be a fully featured add-on to partsbox. This is a tool I am developing for myself to help me manage my inventory. I am not an active developer and this software wont work forever, but I figure it might help someone else if it helps me.

To use it, make sure you have all the dependencies installed, and add your partsbox API key to the secrets file. From there, run main.py and follow the prompts to generate labels for parts. The end result of this program will be a pdf file with one or more labels that you can print. I am using a Brother QL-570 printer with 29mm continuous tape.

The default label generated is a 73mm x 29mm label cut from the continuous tape. There are references to a "magazine" or "compact" label, which is 65mm x 29mm. These labels are designed to fit onto the back of 3D printed SMD tape magazines found here: https://www.thingiverse.com/thing:3952021   credit to Thingiverse user robin7331 for the component storage. 
