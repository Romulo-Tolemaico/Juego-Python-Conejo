class Colision():
    def __init__(self,jugador,zanahoria,animacion,sonido,score) -> None:
        self.jugador = jugador
        self.zanahoria = zanahoria
        self.animacion = animacion  
        self.sonido = sonido
        self.score = score
    
    def detectarMuro(self):
        #Bordes
        if self.jugador.cordY < 95:
            self.jugador.cordY = 96
        if self.jugador.cordY + self.jugador.tamanio > 544:
            self.jugador.cordY = 543 - self.jugador.tamanio

        if self.jugador.cordX < 127:
            self.jugador.cordX = 128
        if self.jugador.cordX + self.jugador.tamanio > 832:
            self.jugador.cordX = 831 - self.jugador.tamanio

    def colisionA(self):
        if self.jugador.cordX >= 128 and self.jugador.cordX <= 319 and self.vertical(160,191):
            self.jugador.cordX = 320
        if self.jugador.cordX >= 288 and self.jugador.cordX  <= 319 and self.vertical(160,479):
            self.jugador.cordX = 320
        if self.jugador.cordX >= 192 and self.jugador.cordX  <= 223 and self.vertical(256,479):
            self.jugador.cordX = 224
        if self.jugador.cordX >= 480 and self.jugador.cordX  <= 511 and self.vertical(256,479):
            self.jugador.cordX = 512
        if self.jugador.cordX >= 384 and self.jugador.cordX  <= 511 and self.vertical(448,479):
            self.jugador.cordX = 512
        if self.jugador.cordX >= 384 and self.jugador.cordX  <= 415 and self.vertical(160,479):
            self.jugador.cordX = 416
        if self.jugador.cordX >= 384 and self.jugador.cordX  <= 607 and self.vertical(160,191):
            self.jugador.cordX = 608
        if self.jugador.cordX >= 576 and self.jugador.cordX  <= 607 and self.vertical(160,575):
            self.jugador.cordX = 608
        if self.jugador.cordX >= 576 and self.jugador.cordX  <= 799 and self.vertical(448,479):
            self.jugador.cordX = 800
        if self.jugador.cordX >= 768 and self.jugador.cordX  <= 799 and self.vertical(160,479):
            self.jugador.cordX = 800
        if self.jugador.cordX >= 672 and self.jugador.cordX  <= 799 and self.vertical(160,191):
            self.jugador.cordX = 800
        if self.jugador.cordX >= 672 and self.jugador.cordX  <= 703 and self.vertical(160,383):
            self.jugador.cordX = 704
        
    
    def colisionD(self):
        if self.jugador.cordX + self.jugador.tamanio >= 288 and self.jugador.cordX + self.jugador.tamanio <= 319 and self.vertical(160,479):
            self.jugador.cordX = 287 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 192 and self.jugador.cordX + self.jugador.tamanio <= 319 and self.vertical(448,479):
            self.jugador.cordX = 191 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 192 and self.jugador.cordX + self.jugador.tamanio <= 223 and self.vertical(256,479):
            self.jugador.cordX = 191 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 480 and self.jugador.cordX + self.jugador.tamanio <= 511 and self.vertical(256,479):
            self.jugador.cordX = 479 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 384 and self.jugador.cordX + self.jugador.tamanio <= 511 and self.vertical(448,479):
            self.jugador.cordX = 383 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 384 and self.jugador.cordX + self.jugador.tamanio <= 415 and self.vertical(160,479):
            self.jugador.cordX = 383 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 384 and self.jugador.cordX + self.jugador.tamanio <= 607 and self.vertical(160,191):
            self.jugador.cordX = 383 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 576 and self.jugador.cordX + self.jugador.tamanio <= 607 and self.vertical(160,575):
            self.jugador.cordX = 575 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 576 and self.jugador.cordX + self.jugador.tamanio <= 799 and self.vertical(448,479):
            self.jugador.cordX = 575 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 768 and self.jugador.cordX + self.jugador.tamanio <= 799 and self.vertical(160,479):
            self.jugador.cordX = 767 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 672 and self.jugador.cordX + self.jugador.tamanio <= 799 and self.vertical(160,191):
            self.jugador.cordX = 671 - self.jugador.tamanio
        if self.jugador.cordX + self.jugador.tamanio >= 672 and self.jugador.cordX + self.jugador.tamanio <= 703 and self.vertical(160,383):
            self.jugador.cordX = 671 - self.jugador.tamanio
        

    def colisionW(self):
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 191 and self.horizontal(128,319):
            self.jugador.cordY = 192
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 479 and self.horizontal(288,319):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 448 and self.jugador.cordY <= 479 and self.horizontal(192,319):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 256 and self.jugador.cordY <= 479 and self.horizontal(480,511):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 448 and self.jugador.cordY <= 479 and self.horizontal(384,511):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 479 and self.horizontal(384,415):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 191 and self.horizontal(384,607):
            self.jugador.cordY = 192
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 575 and self.horizontal(576,607):
            self.jugador.cordY = 576
        if self.jugador.cordY >= 448 and self.jugador.cordY <= 479 and self.horizontal(576,799):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 479 and self.horizontal(768,799):
            self.jugador.cordY = 480
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 191 and self.horizontal(672,799):
            self.jugador.cordY = 192
        if self.jugador.cordY >= 160 and self.jugador.cordY <= 383 and self.horizontal(672,703):
            self.jugador.cordY = 384

    
    def colisionS(self):
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 191 and self.horizontal(128,319):
            self.jugador.cordY = 127
        if self.jugador.cordY + self.jugador.tamanio >= 448 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(192,319):
            self.jugador.cordY = 447 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 256 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(192,223):
            self.jugador.cordY = 255 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 256 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(480,511):
            self.jugador.cordY = 255 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 448 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(384,511):
            self.jugador.cordY = 447 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(384,415):
            self.jugador.cordY = 159 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 191 and self.horizontal(384,607):
            self.jugador.cordY = 159 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 575 and self.horizontal(576,607):
            self.jugador.cordY = 159 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 448 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(576,799):
            self.jugador.cordY = 447 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 479 and self.horizontal(768,799):
            self.jugador.cordY = 159 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 191 and self.horizontal(672,799):
            self.jugador.cordY = 159 - self.jugador.tamanio
        if self.jugador.cordY + self.jugador.tamanio >= 160 and self.jugador.cordY + self.jugador.tamanio <= 383 and self.horizontal(672,307):
            self.jugador.cordY = 159 - self.jugador.tamanio
        
        
        

    def horizontal(self,x1,x2):
        return self.jugador.cordX >= x1 and self.jugador.cordX <= x2 or self.jugador.cordX + self.jugador.tamanio >= x1 and self.jugador.cordX <= x2
    
    def vertical(self,y1,y2):
        return self.jugador.cordY >= y1 and self.jugador.cordY <= y2 or self.jugador.cordY + self.jugador.tamanio >= y1 and self.jugador.cordY <= y2
        
    def detectarItem(self):
        zx = self.zanahoria.cordX
        zy = self.zanahoria.cordY
        zn = self.zanahoria.tamanio
        jx = self.jugador.cordX
        jy = self.jugador.cordY
        jn = self.jugador.tamanio
        if (((jy + jn >= zy and jy + jn <= zy + zn) and  
            ((jx + jn >= zx and jx + jn <= zx + zn) or (jx >= zx and jx <= zx + zn))) or 
            ((jy >= zy and jy <= zy + zn) and 
            ((jx + jn >= zx and jx + jn <= zx + zn) or (jx >= zx and jx <= zx + zn)))):
            self.sonido.iniciarItem()
            self.zanahoria.restablecer()
            self.score.incrementarPuntaje()


    
    def detectarMira(self,mira):
        mx = mira.cordX
        my = mira.cordY
        mn = mira.tamanio
        jx = self.jugador.cordX
        jy = self.jugador.cordY
        jn = self.jugador.tamanio
        if (((jy + jn >= my and jy + jn <= my + mn) and  
            ((jx + jn >= mx and jx + jn <= mx + mn) or (jx >= mx and jx <= mx + mn))) or 
            ((jy >= my and jy <= my + mn) and 
            ((jx + jn >= mx and jx + jn <= mx + mn) or (jx >= mx and jx <= mx + mn)))):
            self.animacion.dibujarMiraTwo(mx,my)
            if(mira.atacar()):
                self.jugador.hp -= mira.danio
                mira.tiempoEspera = 100
                self.sonido.iniciarDisparo()
                self.animacion.dibujarBackGround2()
                if self.jugador.hp < 1:
                    self.jugador.vivo = False
        else:
            self.animacion.dibujarMiraOne(mx,my)
        

    def detectarChoqueMuroGeneralMira(self,mira):
        if mira.cordX >= 831:
            mira.direccionX = 'a'
        elif mira.cordX <= 128:
            mira.direccionX = 'd'
        
        if mira.cordY >= 543:
            mira.direccionY = 'w'
        elif mira.cordY <= 96:
            mira.direccionY = 's'

