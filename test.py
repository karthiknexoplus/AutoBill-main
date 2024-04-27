#!/usr/bin/env python

import cv2
import os
import sys
import signal
import logging
from edge_impulse_linux.image import ImageImpulseRunner

import requests
import json
from requests.structures import CaseInsensitiveDict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

runner = None

id_product = 1  # Initialize the global variable outside of any function or scope

a = 'Apple'
b = 'Banana'
l = 'Lays'
c = 'Coke'


def sigint_handler(sig, frame):
    logger.info('Interrupted')
    if runner:
        runner.stop()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


def post(label, price):
    global id_product
    url = "http://192.168.87.224:5000/"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data_dict = {"id": id_product, "name": label, "price": price,
                 "units": "units"}
    data = json.dumps(data_dict)
    resp = requests.post(url, headers=headers, data=data)
    logger.info(resp.status_code)
    id_product += 1
    time.sleep(1)


def rate(label):
    logger.info("Calculating rate")
    if label == a:
        logger.info("Calculating rate of %s" % label)
        price = 10
        post(label, price)
    elif label == b:
        logger.info("Calculating rate of %s" % label)
        price = 20
        post(label, price)
    elif label == l:
        logger.info("Calculating rate of %s" % label)
        price = 1
        post(label, price)
    else:
        logger.info("Calculating rate of %s" % label)
        price = 2
        post(label, price)


def main(argv):
    try:
        if len(argv) == 0:
            logger.info('Usage: python classify.py <path_to_model.eim>')
            sys.exit(2)

        model = argv[0]

        dir_path = os.path.dirname(os.path.realpath(__file__))
        modelfile = os.path.join(dir_path, model)

        logger.info('MODEL: ' + modelfile)

        with ImageImpulseRunner(modelfile) as runner:
            model_info = runner.init()
            logger.info('Loaded runner for "%s / %s"' % (model_info['project']['owner'], model_info['project']['name']))
            labels = model_info['model_parameters']['labels']

            videoCaptureDeviceId = 0  # Assuming the camera is the first device

            camera = cv2.VideoCapture(videoCaptureDeviceId)
            ret = camera.read()[0]
            if ret:
                backendName = camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                logger.info("Camera %s (%s x %s) selected." % (backendName, h, w))
                camera.release()
            else:
                raise Exception("Couldn't initialize selected camera.")

            next_frame = 0  # limit to ~10 fps here

            for res, img in runner.classifier(videoCaptureDeviceId):
                if next_frame > now():
                    time.sleep((next_frame - now()) / 1000)

                if "classification" in res["result"].keys():
                    logger.info('Result (%d ms.) ' % (res['timing']['dsp'] + res['timing']['classification']))
                    for label in labels:
                        score = res['result']['classification'][label]
                        if score > 0.9:
                            if label == a:
                                logger.info('Apple detected')
                            elif label == b:
                                logger.info('Banana detected')
                            elif label == l:
                                logger.info('Lays detected')
                            else:
                                logger.info('Coke detected')
                            rate(label)
                    logger.info('')
                next_frame = now() + 100
    except Exception as e:
        logger.error(str(e))


if __name__ == "__main__":
    main(sys.argv[1:])
