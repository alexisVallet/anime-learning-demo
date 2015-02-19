""" Module encapsulating the identification server process.
"""
import zmq
import numpy as np
import cPickle as pickle

from cnn_anime.dataset import ListDataset

# Sending and receiving numpy arrays, from pyzmq's documentation.
def recv_array(socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = buffer(msg)
    A = np.frombuffer(buf, dtype=md['dtype'])
    return A.reshape(md['shape'])

def ident_server(sock_name):
    # Loads the model.
    model = None
    with open('models/gap19_spp_thresh.pkl', 'rb') as cnn_file:
        model = pickle.load(cnn_file)
    # Simple identification closure. Expects a fully pre-processed image.
    def identify(img):
        return model.predict_labels_named(
            ListDataset([img], [frozenset([])]),
            batch_size=1,
            method='thresh',
            confidence=True
        )

    # Connect to the socket.
    ctx = zmq.Context.instance()
    sock = ctx.socket(zmq.REP)
    sock.bind(sock_name)
    
    # Waits for images on the socket, processes them, sends the labels.
    # Dead simple.
    while True:
        image = recv_array(sock)
        sock.send_pyobj(identify(image), protocol=pickle.HIGHEST_PROTOCOL)
