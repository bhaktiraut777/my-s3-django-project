# AWS_Learning

A Django-based web application demonstrating image upload, storage, and retrieval using **Amazon S3**. The `awsapp` handles image uploads via web forms and lists the images using secure, expiring S3 URLs.

---

## 🚀 Features

- Upload images from a web form
- Store files securely in an S3 bucket
- Generate **presigned URLs** to access images privately
- View all uploaded images in a gallery
- Clean project structure with environment-based settings
- Extendable to other file operations (delete, list, etc.)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/AWS_Learning.git
cd AWS_Learning
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file or add these to your system environment:


AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-s3-bucket-name
AWS_S3_REGION_NAME=your-region (e.g., us-east-1)
Make sure your AWS IAM user has the following permissions:


{
  "Action": ["s3:PutObject", "s3:GetObject", "s3:ListBucket"],
  "Effect": "Allow",
  "Resource": [
    "arn:aws:s3:::your-s3-bucket-name",
    "arn:aws:s3:::your-s3-bucket-name/*"
  ]
}
🖼️ Upload & View Images
Upload View
URL: /upload/

Upload images via Django form

File is stored on AWS S3 under images/ prefix

Gallery View
URL: /images/

Displays uploaded images using presigned S3 URLs

Images are fetched privately with temporary access

🧠 Key Components
S3Client (in s3_client.py)
Encapsulates all S3 operations:

upload_fileobj(file_obj, s3_key): Uploads a file

list_image_urls(prefix): Lists image URLs

generate_presigned_url(s3_key): Creates temporary download link

🧪 Run Locally

python manage.py runserver
Then open:

http://127.0.0.1:8000/upload/ — to upload images

http://127.0.0.1:8000/images/ — to view uploaded gallery

📦 Deployment Notes
Make sure AWS credentials are securely managed (e.g., via AWS IAM Roles or Secret Managers)

For production, consider using Amazon CloudFront for caching and faster S3 delivery

Enable HTTPS and CORS settings if exposing images to web

🧹 TODO
 Add delete functionality for images

 Paginate image gallery

 Add file-type validation

 Dockerize the app

📄 License
MIT License. Free to use and modify.

🤝 Author
Built by [Satish Raut]
📧 satish.raut777@gamil.com

---

Let me know if:
- You want to include **screenshots** of the upload/gallery pages
- You want a `Dockerfile` or deployment section (EC2, Elastic Beanstalk, etc.)
- You need `requirements.txt` auto-generated

I can adjust the README accordingly.
