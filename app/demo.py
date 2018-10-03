from sdk.process_image import ProcessImage

if __name__ == "__main__":
    img = ProcessImage("./files/cat.png")
    rs = img.process()
    print(rs)
