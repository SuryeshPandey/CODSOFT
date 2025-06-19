# 🧠 AI Image Captioning Web App

An end-to-end image captioning application powered by a pre-trained BLIP model from HuggingFace. Built with a **Flask backend** for AI inference and a **Next.js frontend** for a modern, animated UI experience.

---

## 🚀 Features

- 🎯 **BLIP AI Model** for accurate image captioning
- 🖼️ Upload an image and get a natural language description
- 💻 Full-stack architecture: Flask + React/Next.js + Tailwind CSS
- 🎥 Animated video background and clean UI
- 📡 REST API integration with CORS support

---

## 🗂️ Folder Structure

```
image-captioning-project-react/
├── backend/
│ └── app/
│ └── routes.py # Flask API using BLIP model
│
├── frontend/ # Next.js 15 + Tailwind UI
│ ├── public/ # dog_run.mp4, favicon, etc.
│ └── src/
│ ├── app/
│ │ └── page.js # Main UI logic
│ └── styles/ # Tailwind styles
│
├── requirements.txt # Python dependencies
└── README.md # You're reading it
```

---

## 🛠️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/SuryeshPandey/image-captioning-project-react.git
cd image-captioning-project-react
```
### ✅ 2. Setup Backend (Flask)
```cd backend
pip install -r ../requirements.txt
python app/routes.py
```
Runs on: http://localhost:5000

---
### ✅ 3. Setup Frontend (Next.js)
```
cd ../frontend
yarn install     # or npm install
yarn dev         # or npm run dev
```
Runs on: http://localhost:3000

---
## 🧪 Test the App

1. Visit `http://localhost:3000`
2. Upload an image (e.g., a dog or a landscape)
3. Click **Generate Caption**
4. View the generated result below the image!

---

## 🎓 Technologies Used

| Area        | Stack                                   |
|-------------|------------------------------------------|
| Backend     | Flask, Python, Transformers              |
| AI Model    | Salesforce BLIP                          |
| Frontend    | Next.js, React, Tailwind CSS             |
| Styling     | Tailwind, Hero section, custom overlay   |
| Video BG    | `dog_run.mp4` in `/public`               |

---
## 📌 Credits

- **Model**: [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) on HuggingFace
- **Frontend**: Developed using **Next.js** & **Tailwind CSS**
- **Backend**: Python + Flask for API


---

## 👤 Author

**Suryesh Pandey**  
📍 *B.Sc. Computing, Bennett University*, [LinkedIn](https://www.linkedin.com/in/suryesh-pandey-61b7a2291/)
