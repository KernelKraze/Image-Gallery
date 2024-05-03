import os

def generate_page_htmls(num_pages):
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery {page_num}</title>
    <link href="/.static/css/global.css" type="text/css" rel="stylesheet" />
    <link href="style.css" type="text/css" rel="stylesheet" />
</head>
<body>
    <div class="banner">
        <img src="./wel-come.svg" alt="Welcome Banner" loading="lazy" />
    </div>
    <div class="gallery" id="imageGallery"></div>

    <!-- Modal -->
    <div id="myModal" class="modal">
        <span class="close" aria-label="Close">&times;</span>
        <span class="navigate left" aria-label="Previous">&#10094;</span>
        <span class="navigate right" aria-label="Next">&#10095;</span>
        <div class="modal-content" id="modalContent"></div>
    </div>

    <div class="navigation">
        {previous_button}
        {next_button}
    </div>

    <script src="script.js" defer></script>
</body>
</html>
"""
    for i in range(1, num_pages + 1):
        previous_button = f'<a href="page_{i - 1}.html">Previous</a>' if i > 1 else ""
        next_button = f'<a href="page_{i + 1}.html">Next</a>' if i < num_pages else ""
        html_content = html_template.format(
            page_num=i, previous_button=previous_button, next_button=next_button)
        page_file_path = os.path.join(os.getcwd(), f'page_{i}.html')
        with open(page_file_path, 'w') as f:
            f.write(html_content)


def generate_index_html():
    index_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery Index</title>
    <link href="/.static/css/global.css" type="text/css" rel="stylesheet" />
    <link href="style.css" type="text/css" rel="stylesheet" />
</head>
<body>
    <h1>Welcome to the Image Gallery</h1>
    <a href="page_1.html">Start with Page 1</a>
</body>
</html>
"""
    with open("index.html", "w") as index_file:
        index_file.write(index_html_content)


def main():
    base_dir = os.getcwd()
    media_files = [f for f in os.listdir(base_dir) if f.startswith("media_") and f.endswith(".json")]
    num_pages = len(media_files)
    generate_index_html()
    generate_page_htmls(num_pages)


if __name__ == "__main__":
    main()
