import time
import os
import sys
from typing import Literal
import playwright.sync_api
from playwright.sync_api import sync_playwright
import pydantic

class EnvState(pydantic.BaseModel):
    screenshot: bytes
    url: str

class PlaywrightComputer:
    def __init__(self, screen_size=(1024, 768), initial_url="about:blank", highlight_mouse=True):
        self.screen_size = screen_size
        self.initial_url = initial_url
        self.highlight_mouse_enabled = highlight_mouse
        self._playwright = None
        self._browser = None
        self._page = None

    def __enter__(self):
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=False)
        self._context = self._browser.new_context(viewport={"width": self.screen_size[0], "height": self.screen_size[1]})
        self._page = self._context.new_page()
        self._page.goto(self.initial_url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._browser: self._browser.close()
        if self._playwright: self._playwright.stop()

    def get_state(self) -> EnvState:
        self._page.wait_for_load_state()
        time.sleep(1.0) # Stability wait
        return EnvState(screenshot=self._page.screenshot(), url=self._page.url)

    def click_at(self, x, y):
        self._highlight(x, y)
        self._page.mouse.click(x, y)
        return self.get_state()

    def type_text_at(self, x, y, text, press_enter=True):
        self.click_at(x, y)
        self._page.keyboard.type(text)
        if press_enter: self._page.keyboard.press("Enter")
        return self.get_state()

    def scroll(self, direction, magnitude=800):
        if direction == "down": self._page.keyboard.press("PageDown")
        elif direction == "up": self._page.keyboard.press("PageUp")
        return self.get_state()
    
    def navigate(self, url):
        self._page.goto(url)
        return self.get_state()

    def _highlight(self, x, y):
        if not self.highlight_mouse_enabled: return
        script = f"""() => {{
            const div = document.createElement('div');
            div.style.position = 'fixed'; div.style.left = '{x}px'; div.style.top = '{y}px';
            div.style.width = '20px'; div.style.height = '20px'; div.style.background = 'red';
            div.style.borderRadius = '50%'; div.style.zIndex = '9999'; document.body.appendChild(div);
            setTimeout(() => div.remove(), 1000);
        }}"""
        self._page.evaluate(script)
        time.sleep(0.5)