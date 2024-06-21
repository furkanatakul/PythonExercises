from rembg import remove

inputPath = "gidi2.jpg"
outputPath = "output5.png"

with open(inputPath, 'rb') as i:
    with open(outputPath, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)