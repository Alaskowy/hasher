from rot import Rot13, Rot47
from buffer import Buffer
from EncryptedText import EncryptedText
import pytest


@pytest.mark.buffer
def test_adding_encrypted_text_to_the_buffer():
    """Test checking if encrypted text is correctly added to the buffer."""
    buffer: Buffer = Buffer()
    encrypted_text = EncryptedText(Rot13(), "test13").to_dict()
    encrypted_text_1 = EncryptedText(Rot47(), "test47").to_dict()

    buffer.add(encrypted_text)
    buffer.add(encrypted_text_1)
    result = buffer.peak()

    assert len(result) == 2
    assert not len(result) == 3

    assert encrypted_text in result
    assert encrypted_text_1 in result


@pytest.mark.buffer
def test_adding_list_of_encrypted_words_to_the_buffer():
    """Test checking if list of encrypted words is correctly added to the buffer."""
    buffer: Buffer = Buffer()

    encrypted_text_list = [
        EncryptedText(Rot13(), "test13").to_dict(),
        EncryptedText(Rot47(), "test47").to_dict(),
    ]

    buffer.add_list(encrypted_text_list)

    result = buffer.peak()

    assert encrypted_text_list == result
    assert len(encrypted_text_list) == len(result)
    assert encrypted_text_list[0] == result[0]
    assert encrypted_text_list[1] == result[1]
