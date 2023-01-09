# need to download the libraries before importing
# terminal command for download (pip install qrcode, Image(pip3 for mac))
import qrcode

# function to generate qr code
def generate_qrcode(text):
    # use the imported library to generate a black qr code
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
        
    )
    # add the text data, and specify the properties of QRcode
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    # save the image with any filename of your choice
    img.save('qrimg.png')

# ASK THE USER TO input a url of their choice
url = input("Enter a url:")
# run generate_qrcode
generate_qrcode(url)