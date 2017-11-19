shaders = ["blur.glsl", "pixelate.glsl", "hue.glsl"]
idxShader = 0
pg = None
shade = None
imagen = None
imagen2 = None

def setup():
    global pg, imagen, imagen2, shaders, idxShader, shade
    
    size(800, 640, P2D)
    textSize(22)
    idxShader = 0
    pg = createGraphics(800, 640)
    imagen = loadImage("cyt.jpg")
    imagen2 = loadImage("a.jpg")
    setupShader()


def draw():
    global imagen, shaders, idxShader, pg
    
    pGraphics_draw()
    setShaderParameters()
    shader(shade)
    image(imagen, 0, 0, width, height)
    resetShader()
    image(pg, 0, 0)
    text(shaders[idxShader], 5, 20)


def setupShader():
    global shaders, shade, idxShader
    
    shade = loadShader(shaders[idxShader])


def setShaderParameters():
    global idxShader, shade
    
    if idxShader == 0:
        blur_size = floor(three_rule(100.0, mouseY, float(height)))
        shade.set("sigma", map(mouseX, 0, width, 0, 100.0))
        shade.set("blurSize", int(blur_size))
    
    elif idxShader == 1:
        shade.set("pixels", 0.1 * mouseX, 0.1 * mouseY)
    
    elif idxShader == 2:
        shade.set("hue", map(mouseX, 0, width, 0, TWO_PI))


def pGraphics_draw():
    pg.beginDraw()
    pg.clear()
    pg.strokeWeight(2)
    pg.stroke(255, 100, 0)
    pg.noFill()
    pg.rectMode(CENTER)
    pg.rect(mouseX, mouseY, 80, 80)
    pg.endDraw()


def three_rule(total, var_value, max_value):
    result = total*(var_value/max_value)
    
    return result


def keyPressed():
    global idxShader, shaders, pg
    
    if key == 'n':
        #idxShader = (idxShader + 1) % len(shaders)
        setupShader()