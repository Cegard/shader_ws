shaders = ["blur.glsl", "hue.glsl", "pixelate.glsl"]
idxShader = 0
pg = None
shade = None
imagen = None
imagen2 = None

def setup():
    global pg, imagen, imagen2, shaders, idxShader
    
    size(800, 640, P3D)
    textSize(22)
    fill(0)
    idxShader = 0
    pg = createGraphics(800, 640)
    imagen = loadImage("cyt.jpg")
    imagen2 = loadImage("a.jpg")
    setupShader()


def draw():
    global imagen, shaders, idxShader, pg
    
    setShaderParameters()
    
    #shader(shade);
    image(imagen, 0, 0, width, height)
    text(shaders[idxShader], 5, 20)
    pg.beginDraw()
    #setShaderParameters()
    pg.clear()
    pg.noFill()
    pg.rectMode(CENTER)
    pg.rect(mouseX, mouseY, 80, 80)
    pg.endDraw()
    image(pg, 0, 0)


def setupShader():
    global shaders, shade, idxShader
    
    shade = loadShader(shaders[idxShader])


def setShaderParameters():
    global idxShader, shade
    
    if idxShader == 0:
        shade.set("hue", map(mouseX, 0, width, 0, TWO_PI))
    
    elif idxShader == 1:
        shade.set("pixels", 0.1 * mouseX, 0.1 * mouseY)
    
    elif idxShader == 2:
        shade.set("sigma", map(mouseX, 0, width, 0, 10.0))
        shade.set("blurSize", map(mouseY, 0, height, 0, 30.0))
    
    print("Puntos: ", map(mouseX, 0, width, 0, TWO_PI))


def keyPressed():
    global idxShader, shaders, pg
    
    if key == 'n':
        idxShader = (idxShader + 1) % len(shaders)
        setupShader()
    
    else:
        fill(0)
        pg.ellipse(mouseX, mouseY, 100, 100)