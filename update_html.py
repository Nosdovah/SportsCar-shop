with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all .png with .webp
content = content.replace('.png', '.webp')

# Add loading='lazy' to all img tags
content = content.replace('<img ', '<img loading="lazy" ')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
