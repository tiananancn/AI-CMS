# AI-CMS Intelligent Content Management System 🎯

[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/语言-中文-red.svg)](README_zh.md)
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A lightweight yet powerful Content Management System (CMS) built with Flask, featuring article, video, and image management with a beautiful admin interface, flexible frontend display, advanced drag-and-drop page editor with library integration and cell merging capabilities.

## ✨ Features

### 🎨 Frontend
- **Homepage Display**: Show latest articles, videos, images, and links
- **Configurable Content**: Select specific content to display on homepage with flexible homepage content management
- **Carousel Banner**: Dynamic homepage carousel with sortable banner images
- **Article System**:
  - Article listing (pagination and category filtering)
  - Article detail pages with rich text content
  - Category and tag system
  - Cover image support with picker
- **Video System**:
  - Video listing (pagination and category filtering)
  - Video detail pages (local files and external links)
  - Category and tag system
- **Image System**:
  - Grid gallery display
  - Image detail pages
  - Image download functionality
  - Modal preview
- **Links Section**: Beautiful link cards display with icons or custom images
- **Dynamic Pages**: Visually stunning pages built with grid editor

### 🛠️ Admin Panel
- **Dashboard**: System statistics display
- **Article Management**:
  - Create, edit, delete articles
  - Rich text editor (Quill.js)
  - Article status management (published/draft)
  - Category and tag management
  - Cover image picker with library integration
- **Video Management**:
  - Add, edit, delete videos
  - Support local video files and external links (YouTube, Bilibili, etc.)
  - Video status management
  - Category and tag management
- **Image Management**:
  - Image upload functionality
  - Image preview and library
  - Image information display
  - Category and tag management
- **Link Management**:
  - Add, edit, delete links
  - Support Font Awesome icons or custom images
  - Link categories and descriptions
  - Drag-and-drop sorting
  - Show/hide control
- **Menu Management**: Dynamic navigation menu with hierarchical support (2 levels) and drag-and-drop ordering
- **Homepage Configuration**: Fully customizable homepage layout with hero section
- **Homepage Content Management**: Select and arrange specific content to display on homepage
  - Choose which articles, videos, images, and links appear on homepage
  - Drag-and-drop reordering for custom display order
  - Search and filter content when selecting
- **Carousel Management**:
  - Manage homepage banner images with drag-and-drop sorting
  - Support up to 5 carousel images
  - Select from image library or upload new images
- **Dynamic Pages**: Advanced drag-and-drop page editor with:
  - **Grid Layout Editor**: Visual grid-based page builder (5x5 or 6x6 grid)
  - **9 Element Types**: Text, Image, Video, Quote, Button, Divider, Gallery, Icon, Card
  - **Library Integration**: Select content directly from existing libraries
    - Select images from image library for Image elements
    - Select videos from video library for Video elements
    - Select multiple images from library for Gallery elements
    - Reference articles in Text elements with one click
  - **Cell Merging**: Merge and unmerge grid cells for flexible layouts
    - Select multiple cells (Ctrl/Cmd + click)
    - Merge rectangular selections into larger regions
    - Visual feedback with selection indicators
    - Size indicators on merged cells (e.g., 2x2)
    - Automatic data persistence across saves
- **Multilingual Support**: Complete bilingual support (Chinese/English)
  - **Frontend Language Switching**: Toggle between Chinese and English via globe icon
  - **Backend Language Switching**: Full admin interface in both languages
  - **Dynamic Content Translation**: Menu items and homepage content translate automatically
  - **Session Persistence**: Language preference saved across sessions
  - **Auto-detection**: Automatic browser language detection

### 🌍 Multilingual Support
- **Complete Bilingual System**: Switch freely between Chinese and English
- **Frontend Language Toggle**: Globe icon in navigation bar for instant switching
- **Backend Full Translation**: All admin interface elements in both languages
- **Dynamic Content Translation**:
  - Menu items (首页/Articles, 文章/Videos, etc.)
  - Homepage content (最新文章/Latest Articles, 欢迎来到/Welcome to)
  - Admin sections (仪表盘/Dashboard, 布局管理/Layout Management)
- **Multiple Switching Methods**:
  - Click globe icon in navigation
  - URL switching: `/set_language/en` or `/set_language/zh_CN`
  - Automatic browser language detection (priority: user choice > session > browser > default)
- **Session Persistence**: Language preference saved across page visits
- **Flask-Babel System**: Professional translation management with .po/.mo files

### 📊 RESTful API
Complete RESTful API endpoints:
- `GET /api/articles` - Get all articles
- `GET /api/articles/<slug>` - Get specific article
- `GET /api/videos` - Get all videos
- `GET /api/videos/<slug>` - Get specific video
- `GET /api/images` - Get all images
- `GET /api/images/<slug>` - Get specific image
- `GET /api/links` - Get visible links (frontend)
- `GET /api/admin/links` - Get all links (admin)
- `POST /api/admin/links` - Create new link
- `PUT /api/admin/links/<id>` - Update link
- `DELETE /api/admin/links/<id>` - Delete link
- `POST /api/admin/links/reorder` - Reorder links
- `GET /api/menu-items` - Get menu items
- `GET /api/admin/menu-items` - Get all menu items (admin)
- `GET /api/admin/homepage-config` - Get homepage configuration
- `PUT /api/admin/homepage-config` - Update homepage configuration
- `GET /api/admin/carousel-config` - Get carousel configuration
- `PUT /api/admin/carousel-config` - Update carousel configuration
- `POST /api/admin/images/upload` - Upload new image
- `GET /api/admin/pages/<id>/grid-layout` - Get grid layout with merged cells
- `POST /api/admin/pages/<id>/grid-layout` - Save grid layout with merged cells

## 🚀 Technology Stack

- **Backend Framework**: Flask 3.0.0
- **Database**: SQLite (cms.db)
- **Frontend Framework**: Bootstrap 5
- **Rich Text Editor**: Quill.js
- **Icons**: Font Awesome 6.4.0
- **Image Processing**: Pillow 10.0.0
- **Internationalization**: Flask-Babel
- **Drag-and-Drop**: SortableJS

## 📦 Installation

### Prerequisites
- Python 3.7+
- pip

### Quick Start

1. **Clone the repository**
```bash
git clone <repository-url>
cd cms
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the system**
- Frontend: http://localhost:8080/
- Admin: http://localhost:8080/admin/login
- Default credentials: `admin` / `admin`

## 📁 Project Structure

```
cms/
├── app.py                      # Main Flask application
├── models.py                   # Database models
├── babel.cfg                   # Translation configuration
├── requirements.txt            # Python dependencies
├── README.md                   # English documentation
├── README_zh.md               # Chinese documentation
├── HOMEPAGE_CONTENT_MANAGEMENT.md  # Homepage content management guide
├── MULTILANG_README.md        # Multilingual feature guide
├── GRID_EDITOR_LIBRARY_INTEGRATION.md  # Grid editor library integration guide
├── CELL_MERGE_FEATURE.md      # Cell merging feature guide
├── translations/              # Translation files
│   ├── zh_CN/LC_MESSAGES/     # Chinese translations
│   │   ├── messages.po
│   │   └── messages.mo
│   └── en_US/LC_MESSAGES/     # English translations
│       ├── messages.po
│       └── messages.mo
├── static/                    # Static files
│   └── uploads/              # Uploaded files
│       ├── images/           # Image files
│       ├── videos/           # Video files
│       └── thumbnails/       # Thumbnails
└── templates/                 # Jinja2 templates
    ├── base.html             # Base template
    ├── index.html            # Homepage
    ├── admin/                # Admin templates
    │   ├── base.html
    │   ├── login.html
    │   ├── dashboard.html
    │   ├── articles.html
    │   ├── article_edit.html
    │   ├── videos.html
    │   ├── video_edit.html
    │   ├── images.html
    │   ├── image_upload.html
    │   ├── menu_management.html
    │   ├── links.html
    │   ├── homepage_config.html
    │   ├── homepage_content.html
    │   ├── carousel_management.html
    │   └── dynamic_page_editor.html  # Grid editor with library integration & cell merging
    ├── article_detail.html
    ├── video_detail.html
    ├── image_detail.html
    ├── articles_list.html
    ├── videos_list.html
    ├── images_list.html
    ├── dynamic_page.html
    └── grid_page_display.html
```

## 📖 Usage Guide

### Admin Login
1. Visit `/admin/login`
2. Enter username: `admin`, password: `admin`
3. Click login to access admin panel

### Create an Article
1. After logging in, click "Articles" in the sidebar
2. Click "New Article"
3. Fill in title, content, category, tags, etc.
4. Choose publication status (publish immediately or save as draft)
5. Click "Save Article"

### Add a Video
1. In admin panel, click "Videos"
2. Click "Add Video"
3. Fill in video information
4. Enter video URL (local path or external link)
5. Save video

### Upload Images
1. In admin panel, click "Images"
2. Click "Upload Image"
3. Select image file
4. Fill in image information
5. Upload and save

### Manage Links
1. In admin panel, go to "Layout Management" > "Link Management"
2. Click "Add/Edit Link"
3. Fill in title and URL
4. Optionally add description, icon (Font Awesome class), or category
5. Set visibility and status
6. Drag and drop links to reorder
7. Click "Save Link"

### Homepage Content Management
1. In admin panel, go to "Layout Management" > "Homepage Content Management"
2. Select content for each section:
   - **Articles Section**: Search and select articles to display
   - **Videos Section**: Choose videos to show on homepage
   - **Images Section**: Pick images for display
   - **Links Section**: Select links to feature
3. Use search boxes to filter content
4. Click "+" to add content to selected list
5. Click "×" to remove content from selected list
6. Drag and drop selected items to reorder
7. Click "Save Configuration" to apply changes

### Carousel Management
1. In admin panel, go to "Layout Management" > "Carousel Management"
2. Click "Add Carousel Image"
3. Choose images from library or upload new ones
4. Drag and drop to reorder carousel images
5. Up to 5 images supported
6. Save changes

### Dynamic Page Editor (Grid Layout)
1. In admin panel, go to "Dynamic Pages"
2. Click "Edit" on any page or create a new one
3. Use the grid editor to build your page:
   - **Add Elements**: Drag elements from the palette to the grid
   - **Library Integration**:
     - For **Images**: Click "Select from Library" to choose from existing images
     - For **Videos**: Click "Select from Video Library" to choose from existing videos
     - For **Galleries**: Click "Select Multiple Images" to choose multiple images
     - For **Text**: Click "Reference Article" to insert existing articles
   - **Cell Merging**:
     - Select cells by clicking (use Ctrl/Cmd for multi-select)
     - Click "Merge Cells" to combine selected cells
     - Click "Unmerge Cells" to split merged cells back
     - Visual feedback shows selected cells and merge sizes
4. Save your page

### Language Switching
- **Frontend**: Click the globe icon in the navigation bar
- **URL Switch**: Visit `/set_language/en` or `/set_language/zh_CN`
- **Auto-detection**: System automatically detects browser language preference

## 🔌 API Examples

### Get All Articles
```bash
curl http://localhost:8080/api/articles
```

### Get Specific Article
```bash
curl http://localhost:8080/api/articles/my-first-article
```

### Get All Images
```bash
curl http://localhost:8080/api/images
```

### Get All Links
```bash
curl http://localhost:8080/api/links
```

### Get Homepage Configuration
```bash
curl http://localhost:8080/api/admin/homepage-config
```

### Update Homepage Configuration
```bash
curl -X PUT http://localhost:8080/api/admin/homepage-config \
  -H "Content-Type: application/json" \
  -d '{"config": {...}, "enabled": true}'
```

### Get Grid Layout with Merged Cells
```bash
curl http://localhost:8080/api/admin/pages/1/grid-layout
```

### Save Grid Layout with Merged Cells
```bash
curl -X POST http://localhost:8080/api/admin/pages/1/grid-layout \
  -H "Content-Type: application/json" \
  -d '{"grid": {...}, "mergedCells": {...}}'
```

### Switch to English (via URL)
```bash
curl http://localhost:8080/set_language/en
```

## ⚙️ Configuration

### Change Admin Password
Edit the login validation logic in `app.py`:
```python
if username == 'admin' and password == 'admin':  # Change password here
    session['admin_logged_in'] = True
```

### Modify Database
Edit `models.py`, then delete `cms.db` and restart the application.

### Change Upload File Size Limit
Edit `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # Change to desired size
```

### Add New Translations
1. Mark text for translation:
   - In templates: `{% trans %}Text to translate{% endtrans %}`
   - In Python: `gettext("Text to translate")`
2. Extract translations:
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```
3. Update translation files:
   ```bash
   pybabel update -i messages.pot -d translations
   ```
4. Edit `.po` files to add translations
5. Compile translations:
   ```bash
   pybabel compile -d translations
   ```

## 📝 Development Notes

### Latest Updates (October 2025)

#### 🔧 Core Feature Enhancements
- **Grid Editor Library Integration** ✅ Complete
  - Select content directly from existing libraries when building pages
  - Image elements: Choose from image library with automatic URL/Alt text filling
  - Video elements: Select from video library with one-click URL insertion
  - Gallery elements: Multi-select images from library for batch application
  - Text elements: Reference existing articles with formatted insertion

- **Cell Merging Feature** ✅ Complete
  - Multi-select cells with Ctrl/Cmd + click
  - Merge rectangular selections into larger regions (e.g., 2x2, 3x1)
  - Visual feedback with blue selection indicators
  - Size indicators on merged cells (e.g., "2x2 merged")
  - Persistent merge state across page saves and loads
  - Unmerge cells to split back into individual cells

- **Homepage Content Management** ✅ Complete
  - Select specific articles, videos, images, and links to display on homepage
  - Search and filter content when selecting
  - Drag-and-drop reordering for custom display sequence
  - Add/remove content with + and × buttons
  - Support for all content types (articles, videos, images, links)
  - Configuration saved to database with backward compatibility

- **Carousel Management** ✅ Complete
  - Manage up to 5 homepage banner images
  - Drag-and-drop sorting for custom display order
  - Select from existing image library or upload new images
  - Recommended size: 1920×800 pixels
  - Support formats: JPG, PNG, GIF, WebP

#### 🌍 Internationalization Improvements
- **Complete Multilingual Support** ✅ Fully Implemented
  - Frontend: All static text translated (navigation, buttons, messages)
  - Backend: Complete admin interface in both languages
  - Dynamic Content: Menu items and homepage content translate automatically
  - Translation mapping system for database-driven content
  - All new features include multilingual support from day one

#### 🐛 Bug Fixes & Improvements
- **Menu Management** ✅ Fixed
  - Resolved "Failed to load menus" error
  - Fixed SortableJS initialization issue (was passing array instead of HTMLElement)
  - Menu drag-and-drop now works correctly
  - All 5 default menus display properly (首页, 文章, 视频, 图片, 其它)

#### 🎨 UI/UX Enhancements
- **Enhanced Image Picker**: Article cover image selection with library integration
- **Hierarchical Menu Support**: 2-level menu system with parent-child relationships
- **Drag-and-Drop Everywhere**: Consistent sorting experience across all management pages
- **Visual Feedback**: Selection indicators, size markers, and hover states
- **Modal Integration**: Library selection through intuitive modal dialogs

#### 📚 Documentation & Testing
- **Comprehensive Documentation**: Detailed guides for each new feature
  - `GRID_EDITOR_LIBRARY_INTEGRATION.md` - Library integration guide
  - `CELL_MERGE_FEATURE.md` - Cell merging documentation
  - `CELL_MERGE_QUICK_GUIDE.md` - Quick reference guide
  - `HOMEPAGE_CONTENT_MANAGEMENT.md` - Homepage content guide
  - `MULTILANG_README.md` - Multilingual feature documentation
- **Automated Testing**: Playwright browser automation for validation
- **API Testing**: All endpoints tested and documented

#### 🔄 Version Highlights
- **v3.0** (Oct 2025): Grid editor with library integration & cell merging
- **v2.5** (Oct 2025): Homepage content management & carousel system
- **v2.0** (Oct 2025): Complete multilingual support
- **v1.5** (Oct 2025): Menu management & link system

### Browser Cache Notes
- Frontend changes may require hard refresh (Ctrl+Shift+R)
- Use incognito mode during development to avoid cached content

### File Organization

**Admin Templates**:
- `homepage_content.html` - Homepage content selection interface
- `carousel_management.html` - Carousel image management
- `homepage_config.html` - Homepage layout configuration
- `dynamic_page_editor.html` - Advanced grid editor with library integration and cell merging

**Documentation**:
- `HOMEPAGE_CONTENT_MANAGEMENT.md` - Detailed guide for homepage content management
- `GRID_EDITOR_LIBRARY_INTEGRATION.md` - Grid editor library integration guide
- `CELL_MERGE_FEATURE.md` - Cell merging feature guide
- `CELL_MERGE_QUICK_GUIDE.md` - Quick guide for cell merging
- `FEATURE_COMPLETION_SUMMARY.md` - Summary of completed features

## ⚠️ Important Notes

### Production Deployment
1. Change `SECRET_KEY` in `app.py`
2. Replace SQLite with PostgreSQL/MySQL
3. Implement proper user authentication
4. Add CSRF protection
5. Configure HTTPS
6. Set up cloud storage (AWS S3, etc.)
7. Add caching layer (Redis/Memcached)
8. Implement rate limiting
9. Add logging and monitoring

### File Uploads
- Ensure `static/uploads/` directory has write permissions
- Regularly clean up unused files

### Performance Optimization
- Use CDN for images
- Add caching mechanisms
- Use reverse proxy (Nginx)
- Enable gzip compression

## 🛣️ Development Roadmap

- [ ] User authentication system
- [ ] Multi-user support
- [ ] Comment system
- [ ] SEO optimization
- [ ] Search functionality
- [ ] Theme system
- [ ] Plugin system
- [ ] Additional languages (Japanese, Korean, etc.)
- [ ] RSS feed support
- [ ] Sitemap generation

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Built by taa with Flask and modern web technologies.

---

**Enjoy using AI-CMS!** 🚀

For more details, see:
- [`HOMEPAGE_CONTENT_MANAGEMENT.md`](HOMEPAGE_CONTENT_MANAGEMENT.md) - Homepage content management guide
- [`MULTILANG_README.md`](MULTILANG_README.md) - Multilingual feature guide
- [`GRID_EDITOR_LIBRARY_INTEGRATION.md`](GRID_EDITOR_LIBRARY_INTEGRATION.md) - Grid editor library integration guide
- [`CELL_MERGE_FEATURE.md`](CELL_MERGE_FEATURE.md) - Cell merging feature guide
- [`CELL_MERGE_QUICK_GUIDE.md`](CELL_MERGE_QUICK_GUIDE.md) - Cell merging quick guide
- [`README_zh.md`](README_zh.md) - 中文文档
