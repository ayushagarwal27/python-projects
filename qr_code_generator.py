import qrcode


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_QR(self, file_name: str, foreground_color: str, background_color: str):
        user_input: str = input('Enter text: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=foreground_color, back_color=background_color)
            qr_image.save(file_name)
            print(f'Successfully created! ({file_name})')
        except Exception as e:
            print(f'Error: {e}')


def main():
    myQR = MyQR(30, 2)
    myQR.create_QR('sample.png', 'skyblue', 'black')


if __name__ == '__main__':
    main();
