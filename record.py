import cv2
from utils import CFEVideoConf

def record_video(save_path='saved-media/video.avi', res='720p', fps=24.0):
    cap = cv2.VideoCapture(0)
    config = CFEVideoConf(cap, filepath=save_path, res=res)
    out = cv2.VideoWriter(save_path, config.video_type, fps, config.dims)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture video frame. Exiting...")
                break
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    record_video()
