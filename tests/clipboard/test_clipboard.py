from jabbapylib.clipboard import clipboard as cb

bak_primary = None
bak_clipboard = None

def setup_module(module):
    """Runs once at the beginning."""
    global bak_primary, bak_clipboard
    
    bak_primary = cb.read_primary()
    bak_clipboard = cb.read_clipboard()
    
def teardown_module(module):
    """Runs once at the very end."""
    cb.to_primary(bak_primary)
    cb.to_clipboard(bak_clipboard)
    
#############################################################################

def setup_function(function):
    """Runs before each test function."""
    cb.clear_both_clipboards()
    
#############################################################################

def test_text_to_clipboards():
    text = 'jabbapylib cb test'
    cb.text_to_clipboards(text)
    assert cb.read_primary() == text
    assert cb.read_clipboard() == text
    
def test_to_primary():
    text = "primary test"
    cb.to_primary(text)
    assert cb.read_primary() == text
    
def test_to_clipboard():
    text = "clipboard test"
    cb.to_clipboard(text)
    assert cb.read_clipboard() == text
    
def test_read_primary():
    test_to_primary()
    
def test_read_clipboard():
    test_to_clipboard()
    
def test_clear_both_clipboards():
    test_text_to_clipboards()
    cb.clear_both_clipboards()
    assert cb.read_primary() == ''
    assert cb.read_clipboard() == ''
    
def test_clear_primary():
    test_to_primary()
    cb.clear_primary()
    assert cb.read_primary() == ''
    
def test_clear_clipboard():
    test_to_clipboard()
    cb.clear_clipboard()
    assert cb.read_clipboard() == ''
    