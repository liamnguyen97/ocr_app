import easyocr

# Number of trials to test reproducibility
NUM_TRIALS = 3

def test_reproduce():
    reader = easyocr.Reader(
        ['vi', 'en'],
        gpu=True,
        detect_network="craft",
        model_storage_directory="./model_storage/model",
        download_enabled=False
    )

    filepath = 'examples/receipt.jpg'
    for i in range(NUM_TRIALS):
        if i == 0:
            detection = reader.readtext(filepath)
        else:
            assert reader.readtext(filepath) == detection
            detection = reader.readtext(filepath)
