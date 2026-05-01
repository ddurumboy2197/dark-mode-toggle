import json
import os

class DarkModeToggle:
    def __init__(self):
        self.localStorageKey = 'darkMode'

    def getDarkMode(self):
        if os.path.exists('dark_mode.json'):
            with open('dark_mode.json', 'r') as f:
                return json.load(f)
        else:
            return False

    def setDarkMode(self, value):
        with open('dark_mode.json', 'w') as f:
            json.dump(value, f)

    def toggleDarkMode(self):
        darkMode = self.getDarkMode()
        self.setDarkMode(not darkMode)

    def getCss(self):
        darkMode = self.getDarkMode()
        if darkMode:
            return 'dark-mode'
        else:
            return 'light-mode'

def main():
    darkModeToggle = DarkModeToggle()

    def toggleDarkMode():
        darkModeToggle.toggleDarkMode()
        document.body.classList.toggle('dark-mode', darkModeToggle.getDarkMode())

    document.addEventListener('DOMContentLoaded', function() {
        const darkModeButton = document.getElementById('dark-mode-toggle');
        darkModeButton.addEventListener('click', toggleDarkMode);
        toggleDarkMode();
    });

if __name__ == "__main__":
    main()
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Mode Toggle</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <button id="dark-mode-toggle">Toggle Dark Mode</button>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    transition: background-color 0.5s;
}

.light-mode {
    background-color: #f0f0f0;
}

.dark-mode {
    background-color: #333;
}
```

Buning uchun sizga qo'shimcha ma'lumotlar kerak bo'lsa, quyidagilar:

- `dark_mode.json` fayli yaratib, unda `{"darkMode": false}` yozib qo'yib, keyin `darkModeToggle` obyektining `getDarkMode` metodi orqali faylni o'qib oladi.
- `toggleDarkMode` metodi orqali dark mode holatini o'zgartiradi.
- `getCss` metodi orqali dark mode holatiga asosan CSS klassini qaytaradi.
- `main` funksiyasida dark mode toggle buttoni yaratib, unga `toggleDarkMode` funksiyasini qo'shib, keyin dark mode holatini o'zgartiradi.
- `styles.css` faylida light va dark mode uchun CSS klasslarini yaratib, keyin ularni HTML faylida qo'shib, dark mode holatiga asosan CSS klassini qo'shib, keyin dark mode toggle buttonini yaratib, unga `toggleDarkMode` funksiyasini qo'shib, keyin dark mode holatini o'zgartiradi.
