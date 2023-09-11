import cv2
def open_camera():
    # Abre a câmera padrão (0) ou outra câmera se especificada (1, 2, etc.)
    print('1')
    cap = cv2.VideoCapture('/dev/video1')
    while True:
        # Captura um frame da câmera
        print('2')
        ret, frame = cap.read()
        # Exibe o frame capturado
        cv2.imshow('Camera', frame)
        # Sai do loop se a tecla 'q' for pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    open_camera()

