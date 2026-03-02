<<<<<<< HEAD
import streamlit as st
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from facenet_pytorch import InceptionResnetV1
import os

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="Face Similarity System", layout="centered")
st.title("Face Similarity System")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# Transform
# ---------------------------
transform = transforms.Compose([
    transforms.Resize((160, 160)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# ---------------------------
# Safe Model Loading
# ---------------------------
def load_model():
    st.write("Loading model...")

    model = InceptionResnetV1(pretrained='vggface2').to(device)

    checkpoint_path = "best_model.pth"

    if not os.path.exists(checkpoint_path):
        st.error("best_model.pth not found.")
        st.stop()

    checkpoint = torch.load(checkpoint_path, map_location=device)

    # Case 1: dictionary with keys
    if isinstance(checkpoint, dict) and 'backbone' in checkpoint:
        model.load_state_dict(checkpoint['backbone'])

    # Case 2: direct state_dict
    else:
        model.load_state_dict(checkpoint)

    model.eval()
    st.write("Model Loaded Successfully")

    return model


model = load_model()

# ---------------------------
# Embedding
# ---------------------------
def get_embedding(image):
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        emb = model(image)
    emb = emb.cpu().numpy()[0]
    emb = emb / np.linalg.norm(emb)
    return emb

# ---------------------------
# Upload Section
# ---------------------------
img1_file = st.file_uploader("Upload Image 1", type=["jpg", "png", "jpeg"])
img2_file = st.file_uploader("Upload Image 2", type=["jpg", "png", "jpeg"])

if img1_file and img2_file:
    img1 = Image.open(img1_file).convert("RGB")
    img2 = Image.open(img2_file).convert("RGB")

    st.image([img1, img2], width=250)

    emb1 = get_embedding(img1)
    emb2 = get_embedding(img2)

    similarity = np.dot(emb1, emb2)

    st.subheader("Similarity Score")
    st.metric("Cosine Similarity", f"{similarity:.4f}")

    if similarity > 0.85:
        st.success("Very Likely Same Person")
    elif similarity > 0.70:
        st.info("Likely Same Person")
    else:
        st.error("Likely Different Persons")
=======
import streamlit as st
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from facenet_pytorch import InceptionResnetV1
import os

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="Face Similarity System", layout="centered")
st.title("Face Similarity System")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# Transform
# ---------------------------
transform = transforms.Compose([
    transforms.Resize((160, 160)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# ---------------------------
# Safe Model Loading
# ---------------------------
def load_model():
    st.write("Loading model...")

    model = InceptionResnetV1(pretrained='vggface2').to(device)

    checkpoint_path = "best_model.pth"

    if not os.path.exists(checkpoint_path):
        st.error("best_model.pth not found.")
        st.stop()

    checkpoint = torch.load(checkpoint_path, map_location=device)

    # Case 1: dictionary with keys
    if isinstance(checkpoint, dict) and 'backbone' in checkpoint:
        model.load_state_dict(checkpoint['backbone'])

    # Case 2: direct state_dict
    else:
        model.load_state_dict(checkpoint)

    model.eval()
    st.write("Model Loaded Successfully")

    return model


model = load_model()

# ---------------------------
# Embedding
# ---------------------------
def get_embedding(image):
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        emb = model(image)
    emb = emb.cpu().numpy()[0]
    emb = emb / np.linalg.norm(emb)
    return emb

# ---------------------------
# Upload Section
# ---------------------------
img1_file = st.file_uploader("Upload Image 1", type=["jpg", "png", "jpeg"])
img2_file = st.file_uploader("Upload Image 2", type=["jpg", "png", "jpeg"])

if img1_file and img2_file:
    img1 = Image.open(img1_file).convert("RGB")
    img2 = Image.open(img2_file).convert("RGB")

    st.image([img1, img2], width=250)

    emb1 = get_embedding(img1)
    emb2 = get_embedding(img2)

    similarity = np.dot(emb1, emb2)

    st.subheader("Similarity Score")
    st.metric("Cosine Similarity", f"{similarity:.4f}")

    if similarity > 0.85:
        st.success("Very Likely Same Person")
    elif similarity > 0.70:
        st.info("Likely Same Person")
    else:
        st.error("Likely Different Persons")
>>>>>>> 0d427bd6c4c2bceffd0b3d8b5af8b6cd9ddabcb6
