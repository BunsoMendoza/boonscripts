from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
print(volume.GetMasterVolumeLevel())

##max volume
##volume.SetMasterVolumeLevel(-0.1, None)

##25%
volume.SetMasterVolumeLevel(-21.0, None)