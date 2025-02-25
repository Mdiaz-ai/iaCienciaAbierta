**Proyecto de Ia_Ciencia_Abierta:**

**Pasos a seguir:**

**1.**
Descargar el directorio

**2.**
Descomprimir la carpeta pdfs.zip

**3.**
Abrir un terminal y escribir el siguiente comando:
**docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2 &**
(Para abir un servidor en docker con grobid en segundo plano)

**4.**
En el mismo terminal abierto, nos metemos en la carpeta grobid_client_python
y compilamos mediante **python procesar_pdfs**

**5.**
Una vez procesados nos moveremos a la carpeta salida, donde se habrán generado todos los archivos 
.xml y ahí ejecutamos el comando **python generate_wordcloud.py && python graficar.py && python links.py**(Quizás sea necesario hacer ejecutar los siguientes comandos por si no se tuvieran instaladas las siguientes librerias : 

**pip install wordcloud**

 **pip install matplotlib**
 
 **pip install numpy**
 
 **pip install pillow** 

Así mismo se se está utilizando una version de python anterior a la 3.5 sería necesario también (**pip install xml.etree.ElementTree**).

Una vez ejecutado el comando se habrá generado el archivo **links.txt** con todos los links, se generarán ventanas emergentes con los **wordclouds** de cada pdf y por último aparecerá un **diagrama de barras** en el cual se incluirán la cantidad de imagen por cada pdf.

