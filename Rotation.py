
def Calc_Interface(img,cc=np.array([128,0,0]),plot=False):
    """Funktion berechnet die Grenzfläche basierend auf dem Color Code der Maske
    und gibt die x,y Pixelkoordinaten zurück

    Args:
        img (_np.array_): _description_
        cc (_np.array_): color code
    """
    
    # Es wird in jeder Spalte nach dem Color Code (cc) gesucht und der minimale Y-Wert bestimmt
    # !!! Achsenrichtung in images beachten !!!
    tmp_array_1,tmp_array_2 = np.where((img[:,:,0]==cc[0]) & (img[:,:,1]==cc[1]) & (img[:,:,2]==cc[2]))
    Coordinates_tmp = np.vstack((tmp_array_2,tmp_array_1)).T
    Coordinates_tmp = Coordinates_tmp[np.lexsort((Coordinates_tmp[:,1],Coordinates_tmp[:,0]))]
    Coordinates_tmp = Coordinates_tmp[np.unique(Coordinates_tmp[:,0],return_index=True)[1]]
    
    # Wenn die Variable plot den Wert True hat, wird das Interface als weiße Linie geplottet
    if plot:
        img_print = img.copy()
        for ind in np.flip(Coordinates_tmp):
            img_print[tuple(ind)] = np.array([255,255,255])
            img_print[tuple(ind+np.array([1,0]))] = np.array([255,255,255])
            img_print[tuple(ind+np.array([-1,0]))] = np.array([255,255,255])
            
        plt.imshow(img_print)
    
    
    return(Coordinates_tmp)

def Calc_Angle(Coordinates,img,plot=False):
    """Funktion berechnet auf Basis der Interface Koordinaten eine Auslgeichsgrade.
    Anschließend wird der Winkel bestimmt und eine Rotationsmatrix errechnet um die Rotation zu korrigieren.

    Args:
        Coordinates (_np.array_): Numpy array welches die Punktkoordinaten im Format [[x1,y1],[x2,y2]..] enthält
        img (_np.array_): Numpy array welche das Bild der Maske enthält
        plot (bool, optional): Plotet optional das Bild mit enthaltener Ausgleichgeraden
        
        
    Return:
        Gibt das Rotatierte Bild, den Rotationswinkel sowie die Parameter der Graden (m,b) zurück.
    """
    
    # Bestimmen der Dimensionen des Images
    rows,cols,_ = img.shape
    
    # Bestimmung der Steigung und des Sekantenabschnittes durch polyfit Funktion
    # Achsrichtung in Y-Richtung beachten!
    m,b = np.polyfit(Coordinates[:,0], Coordinates[:,1], 1)

    # Berechnung des Winkels aus der Geradensteigung
    alpha = np.rad2deg(np.arctan(m))

    # Aufstellen einer Rotationsmatrix und Rotieren des Bildes
    M = cv2.getRotationMatrix2D((cols/2,rows/2),alpha,1) 
    rotate = cv2.warpAffine(img,M,(cols,rows))
    
    # Wenn die Variable plot den Wert True hat, wird die berechnete Ausgleichsgrade geplottet
    if plot:
        p1 = np.rint(np.array([0,b])).astype(int)
        p2 = np.rint(np.array([img.shape[1],img.shape[1]*m+b])).astype(int)
        img_line = cv2.line(img,p1,p2,(255,255,255),3)
        plt.imshow(img_line)
    
    return(rotate,alpha,(m,b))
