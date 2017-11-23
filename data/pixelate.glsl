#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

varying vec4 vertTexCoord;
uniform sampler2D texture;
uniform vec2 pixels;
uniform float pixelX;
uniform float xLength;
uniform float pixelY;
uniform float yLength;


bool isInBounds(float pixelComp, float compValue, float length){
	bool result = (pixelComp >= (compValue - length)) && (pixelComp <= (compValue + length));
	
	return result;
}


void main(void){
  	vec2 p = vertTexCoord.st;
	
	bool isXInBounds = isInBounds(gl_FragCoord.x, pixelX, xLength);
	bool isYInBounds = isInBounds(gl_FragCoord.y, pixelY, yLength);

	if (isXInBounds && isYInBounds){
		p.x -= mod(p.x, 1.0 / pixels.x);
		p.y -= mod(p.y, 1.0 / pixels.y);
		
		vec3 col = texture2D(texture, p).rgb;
		gl_FragColor = vec4(col, 1.0);
	}
	
	else
		gl_FragColor = texture2D(texture, p);
}
