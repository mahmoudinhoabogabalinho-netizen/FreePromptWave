# FreePromptWave | موجة البرومبت المجانية 🌊

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.0+-green.svg)](https://vuejs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-red.svg)](https://flask.palletsprojects.com/)

## مقدمة | Introduction

**العربية:**  
موجة البرومبت المجانية هو مشروع مفتوح المصدر لإدارة ومشاركة البرومبت (الاستعلامات) الخاصة بالذكاء الاصطناعي. يهدف المشروع إلى توفير منصة مجانية وسهلة الاستخدام لتخزين وتنظيم ومشاركة البرومبت المفيدة مع المجتمع.

**English:**  
FreePromptWave is a free and open-source project for managing and sharing AI prompts. The project aims to provide a free and easy-to-use platform for storing, organizing, and sharing useful prompts with the community.

## الميزات | Features

### العربية:
- 🔍 البحث في البرومبت بسهولة
- 📝 إضافة برومبت جديدة
- 🏷️ تصنيف البرومبت حسب الفئات
- 💾 حفظ البرومبت في قاعدة بيانات محلية
- 🌐 واجهة ويب تفاعلية باللغتين العربية والإنجليزية
- 🚀 سهولة النسخ والاستخدام
- 📱 تصميم متجاوب يعمل على جميع الأجهزة
- ⭐ نظام الإعجاب والتقييم
- 👁️ تتبع عدد المشاهدات

### English:
- 🔍 Easy search through prompts
- 📝 Add new prompts
- 🏷️ Categorize prompts by type
- 💾 Store prompts in local database
- 🌐 Interactive web interface in Arabic and English
- 🚀 Easy copy and use
- 📱 Responsive design that works on all devices
- ⭐ Like and rating system
- 👁️ View count tracking

## هيكل المشروع | Project Structure

```
FreePromptWave/
├── frontend/                    # التطبيق الأمامي | Frontend Application
│   ├── src/
│   │   ├── main.js             # نقطة الدخول | Entry Point
│   │   ├── App.vue             # المكون الرئيسي | Main Component
│   │   └── components/
│   │       └── PromptList.vue  # مكون قائمة البرومبت | Prompt List Component
│   └── package.json            # إعدادات Vue.js | Vue.js Configuration
├── backend/                     # الخادم الخلفي | Backend Server
│   ├── app.py                  # خادم Flask | Flask Server
│   ├── requirements.txt        # متطلبات Python | Python Dependencies
│   └── prompts_store.json      # قاعدة البيانات | Database File
└── README.md                   # هذا الملف | This File
```

## التقنيات المستخدمة | Technologies Used

### الواجهة الأمامية | Frontend:
- **Vue.js 3** - إطار عمل JavaScript تفاعلي | Reactive JavaScript Framework
- **HTML5 & CSS3** - هيكل وتنسيق الصفحات | Page Structure and Styling
- **JavaScript ES6+** - منطق التطبيق | Application Logic

### الخادم الخلفي | Backend:
- **Python Flask** - خادم الويب | Web Server
- **Flask-CORS** - دعم الطلبات عبر المصادر | Cross-Origin Request Support
- **JSON** - تخزين البيانات | Data Storage

## التثبيت والتشغيل | Installation and Setup

### متطلبات النظام | System Requirements
- Python 3.8+
- Node.js 16+ (للتطوير)
- متصفح ويب حديث | Modern Web Browser

### 1. تحميل المشروع | Clone the Project

```bash
git clone https://github.com/mahmoudinhoabogabalinho-netizen/FreePromptWave.git
cd FreePromptWave
```

### 2. تشغيل الخادم الخلفي | Run Backend Server

```bash
# الانتقال إلى مجلد الخادم الخلفي | Navigate to backend folder
cd backend

# تثبيت المتطلبات | Install dependencies
pip install -r requirements.txt

# تشغيل الخادم | Run the server
python app.py
```

الخادم سيعمل على: `http://localhost:5000`  
The server will run on: `http://localhost:5000`

### 3. تشغيل الواجهة الأمامية | Run Frontend Application

```bash
# الانتقال إلى مجلد الواجهة الأمامية | Navigate to frontend folder
cd frontend

# تثبيت المتطلبات | Install dependencies
npm install

# تشغيل خادم التطوير | Run development server
npm run dev
```

التطبيق سيعمل على: `http://localhost:3000`  
The application will run on: `http://localhost:3000`

## الاستخدام | Usage

### إضافة برومبت جديد | Adding a New Prompt
1. افتح التطبيق في متصفحك | Open the app in your browser
2. املأ النموذج بالمعلومات المطلوبة | Fill out the form with required information
3. اضغط على "إضافة" | Click "Add Prompt"

### البحث في البرومبت | Searching Prompts
1. استخدم شريط البحث في أعلى الصفحة | Use the search bar at the top of the page
2. ابحث بالعنوان أو المحتوى أو الفئة | Search by title, content, or category

### نسخ البرومبت | Copying Prompts
1. اضغط على زر "نسخ" في البرومبت المطلوب | Click the "Copy" button on the desired prompt
2. البرومبت سيتم نسخه إلى الحافظة | The prompt will be copied to clipboard

## API التطبيق | Application API

### النقاط النهائية | Endpoints

#### `GET /api/prompts`
الحصول على جميع البرومبت | Get all prompts

#### `POST /api/prompts`
إضافة برومبت جديد | Add a new prompt

**نموذج الطلب | Request Body:**
```json
{
  "title": "عنوان البرومبت | Prompt Title",
  "content": "محتوى البرومبت | Prompt Content",
  "category": "الفئة | Category",
  "tags": ["تاغ1", "تاغ2"],
  "author": "اسم المؤلف | Author Name"
}
```

#### `GET /api/prompts/search?q=query&category=category`
البحث في البرومبت | Search prompts

#### `GET /api/prompts/{id}`
الحصول على برومبت محدد | Get specific prompt

#### `POST /api/prompts/{id}/like`
إضافة إعجاب للبرومبت | Like a prompt

## المساهمة | Contributing

### العربية:
نرحب بالمساهمات من المجتمع! إذا كنت تريد المساهمة:

1. اعمل Fork للمشروع
2. أنشئ فرع جديد للميزة الخاصة بك
3. اعمل commit للتغييرات
4. ادفع التغييرات إلى الفرع الخاص بك
5. افتح Pull Request

### English:
We welcome contributions from the community! If you want to contribute:

1. Fork the project
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## المشاكل والاقتراحات | Issues and Suggestions

إذا واجهت أي مشاكل أو لديك اقتراحات، يرجى فتح Issue في GitHub.  
If you encounter any issues or have suggestions, please open an Issue on GitHub.

## الترخيص | License

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## الشكر والتقدير | Acknowledgments

- شكر خاص لمجتمع المطورين العرب | Special thanks to the Arab developer community
- شكر لجميع المساهمين في هذا المشروع | Thanks to all contributors to this project
- مستوحى من الحاجة لمنصة عربية لمشاركة البرومبت | Inspired by the need for an Arabic platform for prompt sharing

## الاتصال | Contact

إذا كان لديك أي أسئلة أو استفسارات، لا تتردد في التواصل معنا.  
If you have any questions or inquiries, feel free to contact us.

**GitHub:** [mahmoudinhoabogabalinho-netizen](https://github.com/mahmoudinhoabogabalinho-netizen)  
**المشروع:** [FreePromptWave](https://github.com/mahmoudinhoabogabalinho-netizen/FreePromptWave)

---

<div align="center">
  <b>صنع بـ ❤️ للمجتمع العربي والعالمي | Made with ❤️ for the Arab and global community</b>
</div>
