import cv2
import numpy as np

c = cv2.VideoCapture(1)
while True:
        _, frame = c.read()
        # Converte o frame capturado para escala de cinza
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Defina os intervalos de cores para a cor vermelha (em formato BGR)
        lower_red = np.array([0, 0, 100])
        upper_red = np.array([50, 50, 255])
        # Cria uma máscara onde os tons de vermelho estejam dentro do intervalo
        red_mask = cv2.inRange(frame, lower_red, upper_red)
        # Aplica a máscara para o frame original para destacar as áreas vermelhas
        red_highlight = cv2.bitwise_and(frame, frame, mask=red_mask)
        # Converte o resultado destacado em escala de cinza
        red_highlight_gray = cv2.cvtColor(red_highlight, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Camera - Cinza com Destaque Vermelho', red_highlight_gray)
        if cv2.waitKey(5)==27:
          break
 
cv2.destroyAllWindows()
