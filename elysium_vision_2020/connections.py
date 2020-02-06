import cv2

from .configurations import *

ROBOT_NETWORK_TABLES_CONNECTION = ovl.NetworkTablesConnection(TEAM_NUMBER, table_name=NETWORK_TABLES_TABLE)
CAMERA = cv2.VideoCupture(0)
