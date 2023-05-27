def crearTabla (dataFrame, nombreTabla):
    archivoHTML = dataFrame.to_html()
    archivo = open(f"./tables/{nombreTabla}.html","w")
    archivo.write('''
                  
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>tablas</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"></head>
        <body>
    
    ''')
    
    archivo.write(archivoHTML)
    
    archivo.write('''
                  
    </body>
</html>
    ''')
    
    archivo.write(archivoHTML)
    archivo.close()