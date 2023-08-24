import easyocr


def test_output_format():
    reader = easyocr.Reader(
        ['vi', 'en'],
        gpu=True,
        detect_network="craft",
        model_storage_directory="./model_storage/model",
        download_enabled=False
    )

    filepath = 'examples/receipt.jpg'
    detection = reader.readtext(filepath)
    assert len(detection[0]) == 3