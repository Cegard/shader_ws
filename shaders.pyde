shaders = ["blur.glsl", "pixelate.glsl", "hue.glsl"]
idxShader = 0
rect_length = 80
rect_height = 80
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
    
    background(0)
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


def three_rule(total, var_value, max_value):
    result = total*(var_value/max_value)
    
    return result


def setShaderParameters():
    global idxShader, shade, rect_length
    
    mouse_x = float(mouseX)
    mouse_y = float(height - mouseY)
    x_length = float(rect_length/2)
    y_length = float(rect_height/2)
    shade.set("pixelX", mouse_x)
    shade.set("xLength", x_length)
    shade.set("pixelY", mouse_y)
    shade.set("yLength", y_length)
    
    if idxShader == 0:
        blur_size =  80 #floor(three_rule(100.0, mouseY, float(height)))
        sigma = 100.0 #three_rule(100, mouseX, float(width))
        shade.set("sigma", sigma)
        shade.set("blurSize", int(blur_size))
    
    elif idxShader == 1:
        shade.set("pixels", 0.1 * mouseX, 0.1 * mouseY)
    
    elif idxShader == 2:
        shade.set("hue", map(mouseX, 0, width, 0, TWO_PI))


def keyPressed():
    global idxShader, shaders, pg
    
    if key == 'n':
        #idxShader = (idxShader + 1) % len(shaders)
        setupShader()


def pGraphics_draw():
    global rect_length, rect_height
    
    pg.beginDraw()
    pg.clear()
    pg.strokeWeight(2)
    pg.stroke(255, 100, 0)
    pg.noFill()
    pg.rectMode(CENTER)
    pg.rect(mouseX, mouseY, rect_length, rect_height)
    pg.endDraw()