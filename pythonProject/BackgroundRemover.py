from rembg import remove

inputPath = "hq720.jpg"
outputPath = "output1.png"

with open(inputPath, 'rb') as i:
    with open(outputPath, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)