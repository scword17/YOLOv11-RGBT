import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v9-RGBT/yolov9s-RGBT-scorefusion.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data=R'ultralytics/cfg/datasets/LLVIP_r20.yaml',
                cache=False,
                imgsz=640,
                epochs=10,
                batch=16,
                close_mosaic=0,
                workers=2,
                device='0',
                optimizer='SGD',  # using SGD
                # resume='', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                use_simotm="RGBT",
                channels=4,
                project='runs/LLVIP_r20',
                name='LLVIP_r20-yolov9s-RGBT-scorefusion',
                )