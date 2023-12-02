from pydantic import BaseModel, ConfigDict, SkipValidation
from pyshark.packet.layers.xml_layer import XmlLayer

class PacketRef(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, skip_validation=True)

    layers : list[XmlLayer]
    frame_info : XmlLayer
    number : int
    interface_captured : str | None
    captured_length : int
    length : int
    sniff_timestamp : str


