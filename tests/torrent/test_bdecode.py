from jabbapylib.torrent import bdecode
import jabbapylib.config as cfg

FILE = cfg.TEST_ASSETS_DIR + '/ubuntu.torrent'


def test_bdecoder():
    torrent = bdecode.BDecoder(FILE)
    assert torrent.name == 'ubuntu-11.10-desktop-amd64.iso'
    assert torrent.length == 731164672