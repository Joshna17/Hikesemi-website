import re, os

BASE = r'C:\Users\HP\hiksemi'

# ── New CSS to append to styles.css ──────────────────────────────────────────
NEW_CSS = """

/* =============================================
   OUTFIT FONT + UPDATED DESIGN TOKENS
============================================= */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

:root {
  --red: #d7000f;
  --red-dark: #b5000d;
  --inner: 1280px;
}

/* =============================================
   ANNOUNCE BAR
============================================= */
.announce-bar {
  background: #d7000f;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;
  overflow: hidden;
}
.announce-bar p {
  font-family: 'Outfit', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: #fff;
  letter-spacing: 0.3px;
  white-space: nowrap;
}
.announce-bar a {
  font-family: 'Outfit', sans-serif;
  font-size: 12px;
  font-weight: 700;
  color: rgba(255,255,255,0.8);
  text-decoration: underline;
  text-underline-offset: 2px;
  white-space: nowrap;
}
.announce-bar a:hover { color: #fff; }

/* =============================================
   NAVBAR (NEW)
============================================= */
.navbar {
  position: sticky;
  top: 0;
  z-index: 999;
  background: #fff;
  border-bottom: 1px solid #ebebeb;
}
.nav-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1920px;
  margin: 0 auto;
  padding: 20px 55px;
}
.nav-logo img { width: 108px; height: 16px; display: block; object-fit: contain; }
.nav-links { display: flex; align-items: center; gap: 0; }
.nav-item { position: relative; }
.nav-link {
  font-family: 'Outfit', sans-serif;
  font-weight: 500;
  font-size: 16px;
  color: #5c5c72;
  padding: 8px 18px;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: color 0.2s;
  white-space: nowrap;
}
.nav-link:hover { color: #0a0a0f; }
.nav-link .chev { width: 12px; height: 12px; transition: transform 0.2s; }
.nav-item:hover .chev { transform: rotate(180deg); }

/* Mega menu */
.mega-menu {
  display: none;
  position: absolute;
  top: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%);
  width: 820px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 16px 60px rgba(0,0,0,0.12);
  border: 1px solid #ebebeb;
  overflow: hidden;
}
.nav-item:hover .mega-menu { display: flex; }
.mega-sidebar {
  width: 200px;
  background: #f7f7f9;
  padding: 16px 0;
  flex-shrink: 0;
}
.mega-sidebar-item {
  display: block;
  padding: 10px 20px;
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #5c5c72;
  transition: background 0.15s, color 0.15s;
  cursor: pointer;
}
.mega-sidebar-item:hover,
.mega-sidebar-item.active { background: #ededf0; color: #0a0a0f; }
.mega-content {
  flex: 1;
  padding: 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
}
.mega-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 10px;
  transition: background 0.15s;
}
.mega-link:hover { background: #f7f7f9; }
.mega-link-icon {
  width: 36px; height: 36px;
  background: #f0f0f4;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}
.mega-link-text { font-family: 'Outfit', sans-serif; }
.mega-link-name { font-size: 14px; font-weight: 600; color: #0a0a0f; display: block; }
.mega-link-sub  { font-size: 12px; color: #9898a8; display: block; }

/* Simple dropdown */
.simple-drop {
  display: none;
  position: absolute;
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 12px 48px rgba(0,0,0,0.1);
  border: 1px solid #ebebeb;
  padding: 8px;
  min-width: 180px;
}
.nav-item:hover .simple-drop { display: block; }
.simple-drop a {
  display: block;
  padding: 8px 14px;
  font-family: 'Outfit', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #5c5c72;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}
.simple-drop a:hover { background: #f7f7f9; color: #0a0a0f; }

.nav-actions { display: flex; align-items: center; gap: 12px; }
.nav-search-btn {
  width: 38px; height: 38px;
  border-radius: 50%;
  border: 1px solid #e8e8e8;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: border-color 0.2s, background 0.2s;
}
.nav-search-btn:hover { background: #f7f7f9; border-color: #c8c8c8; }
.nav-contact-btn {
  background: #d7000f;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-weight: 600;
  font-size: 15px;
  padding: 13px 16px;
  border-radius: 8px;
  border: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: background 0.2s;
  text-decoration: none;
}
.nav-contact-btn:hover { background: #b5000d; }

/* =============================================
   FOOTER (NEW)
============================================= */
.footer { background: #000; overflow: hidden; }
.footer-main {
  padding: 64px 102px 0;
  max-width: 1716px;
  margin: 0 auto;
  display: flex;
  gap: 80px;
  align-items: flex-start;
}
.footer-brand { flex: 0 0 280px; }
.footer-logo { margin-bottom: 18px; }
.footer-logo img { height: 15px; width: auto; display: block; }
.footer-tagline {
  font-family: 'Outfit', sans-serif;
  font-weight: 300;
  font-size: 16px;
  color: #555;
  line-height: 23.8px;
  margin-bottom: 28px;
  max-width: 250px;
}
.footer-socials { display: flex; gap: 10px; }
.footer-social-btn {
  width: 36px; height: 36px;
  background: #0f0f0f;
  border: 1px solid #212121;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  font-size: 12px;
  color: #555;
  transition: border-color 0.2s, color 0.2s;
  cursor: pointer;
  text-decoration: none;
}
.footer-social-btn:hover { border-color: #444; color: #888; }
.footer-cols {
  flex: 1;
  display: flex;
  justify-content: space-between;
}
.footer-col { flex: 0 0 auto; }
.footer-col-title {
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 1.32px;
  color: #fff;
  text-transform: uppercase;
  margin-bottom: 32px;
}
.footer-col-links { display: flex; flex-direction: column; gap: 24px; }
.footer-col-links a {
  font-family: 'Outfit', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #555;
  transition: color 0.2s;
  display: block;
}
.footer-col-links a:hover { color: #888; }
.footer-bottom-bar {
  max-width: 1716px;
  margin: 32px auto 0;
  padding: 32px 102px 31px;
  border-top: 1px solid #121212;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.footer-copy,
.footer-contact-info {
  font-family: 'Outfit', sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #333;
}
.footer-decoration { width: 100%; display: block; height: auto; }

/* =============================================
   RESPONSIVE – NAVBAR + FOOTER
============================================= */
@media (max-width: 1100px) {
  .nav-wrap { padding: 16px 32px; }
}
@media (max-width: 992px) {
  .footer-main { flex-direction: column; gap: 40px; padding: 48px 32px 0; }
  .footer-cols  { flex-wrap: wrap; gap: 32px; }
  .footer-bottom-bar { padding: 24px 32px; flex-direction: column; gap: 8px; text-align: center; }
}
@media (max-width: 768px) {
  .announce-bar { display: none; }
  .nav-links    { display: none; }
  .nav-wrap     { padding: 16px 24px; }
  .footer-cols  { gap: 24px; }
}
"""

# ── New announce bar + navbar HTML ────────────────────────────────────────────
NEW_NAV = """  <div class="announce-bar">
    <p>Free shipping on orders over $49 — Worldwide delivery available</p>
    <a href="products.html">Shop Now →</a>
  </div>

  <!-- ============ NAVBAR ============ -->
  <nav class="navbar">
    <div class="nav-wrap">
      <a href="index.html" class="nav-logo">
        <img src="images/logo.png" alt="HIKSEMI" />
      </a>
      <div class="nav-links">
        <div class="nav-item">
          <a href="products.html" class="nav-link">
            Products
            <svg class="chev" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M2 4L6 8L10 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          <div class="mega-menu">
            <div class="mega-sidebar">
              <span class="mega-sidebar-item active">All Products</span>
              <span class="mega-sidebar-item">SSD</span>
              <span class="mega-sidebar-item">Memory</span>
              <span class="mega-sidebar-item">Memory Cards</span>
              <span class="mega-sidebar-item">External Storage</span>
              <span class="mega-sidebar-item">NAS</span>
            </div>
            <div class="mega-content">
              <a href="product-details.html" class="mega-link">
                <div class="mega-link-icon">💾</div>
                <div class="mega-link-text">
                  <span class="mega-link-name">FUTURE CORE Gen5 NVMe</span>
                  <span class="mega-link-sub">PCIe 5.0 · Up to 2TB</span>
                </div>
              </a>
              <a href="products.html" class="mega-link">
                <div class="mega-link-icon">🧠</div>
                <div class="mega-link-text">
                  <span class="mega-link-name">FUTURE RGB DDR5</span>
                  <span class="mega-link-sub">6000MHz · 32GB Kit</span>
                </div>
              </a>
              <a href="products.html" class="mega-link">
                <div class="mega-link-icon">📷</div>
                <div class="mega-link-text">
                  <span class="mega-link-name">CAPTURE V90 SD Card</span>
                  <span class="mega-link-sub">V90 · 280 MB/s</span>
                </div>
              </a>
              <a href="products.html" class="mega-link">
                <div class="mega-link-icon">📦</div>
                <div class="mega-link-text">
                  <span class="mega-link-name">ELITE 7S Portable SSD</span>
                  <span class="mega-link-sub">2,000 MB/s · 4TB</span>
                </div>
              </a>
              <a href="products.html" class="mega-link">
                <div class="mega-link-icon">🎮</div>
                <div class="mega-link-text">
                  <span class="mega-link-name">FUTURE PRO microSD Express</span>
                  <span class="mega-link-sub">800 MB/s · Gaming</span>
                </div>
              </a>
              <a href="products.html" class="mega-link">
                <div class="mega-link-icon">🖥️</div>
                <div class="mega-link-text">
                  <span class="mega-link-name">AFS-R1 Home NAS</span>
                  <span class="mega-link-sub">2-Bay · 32TB Max</span>
                </div>
              </a>
            </div>
          </div>
        </div>
        <div class="nav-item">
          <a href="solutions.html" class="nav-link">Solutions</a>
        </div>
        <div class="nav-item">
          <a href="company.html" class="nav-link">Company</a>
        </div>
        <div class="nav-item">
          <a href="support.html" class="nav-link">Support</a>
        </div>
        <div class="nav-item">
          <a href="where-to-buy.html" class="nav-link">
            Our Partners
            <svg class="chev" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M2 4L6 8L10 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
          <div class="simple-drop">
            <a href="where-to-buy.html">Where to Buy</a>
            <a href="where-to-buy.html#distributors">Distributors</a>
            <a href="where-to-buy.html#online">Online Retailers</a>
          </div>
        </div>
      </div>
      <div class="nav-actions">
        <button class="nav-search-btn" aria-label="Search">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="8" cy="8" r="5.5" stroke="#5c5c72" stroke-width="1.5"/>
            <path d="M12.5 12.5L16 16" stroke="#5c5c72" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </button>
        <a href="contact.html" class="nav-contact-btn">Contact →</a>
      </div>
    </div>
  </nav>"""

# ── New footer HTML ───────────────────────────────────────────────────────────
NEW_FOOTER = """  <!-- ============ FOOTER ============ -->
  <footer class="footer">
    <div class="footer-main">
      <div class="footer-brand">
        <div class="footer-logo">
          <img src="images/logo.png" alt="HIKSEMI" />
        </div>
        <p class="footer-tagline">Global provider of high-performance storage solutions for every application — from gaming to enterprise.</p>
        <div class="footer-socials">
          <a href="#" class="footer-social-btn">f</a>
          <a href="#" class="footer-social-btn">in</a>
          <a href="#" class="footer-social-btn">tw</a>
          <a href="#" class="footer-social-btn">yt</a>
          <a href="#" class="footer-social-btn">ig</a>
        </div>
      </div>
      <div class="footer-cols">
        <div class="footer-col">
          <div class="footer-col-title">Products</div>
          <div class="footer-col-links">
            <a href="product-details.html">FUTURE CORE SSD</a>
            <a href="products.html">Memory (RAM)</a>
            <a href="products.html">Memory Cards</a>
            <a href="products.html">External Storage</a>
            <a href="products.html">Home NAS</a>
            <a href="products.html">Embedded Storage</a>
          </div>
        </div>
        <div class="footer-col">
          <div class="footer-col-title">Company</div>
          <div class="footer-col-links">
            <a href="company.html">About HIKSEMI</a>
            <a href="company.html">Why HIKSEMI</a>
            <a href="#">News</a>
            <a href="company.html">Quality</a>
            <a href="where-to-buy.html">Partners</a>
          </div>
        </div>
        <div class="footer-col">
          <div class="footer-col-title">Solution</div>
          <div class="footer-col-links">
            <a href="solutions.html">Gaming</a>
            <a href="solutions.html">Content Creation</a>
            <a href="solutions.html">Industrial</a>
            <a href="solutions.html">Surveillance</a>
            <a href="solutions.html">Enterprise</a>
          </div>
        </div>
        <div class="footer-col">
          <div class="footer-col-title">Support</div>
          <div class="footer-col-links">
            <a href="support.html">Support Home</a>
            <a href="support.html">Warranty</a>
            <a href="support.html">FAQ</a>
            <a href="support.html">Downloads</a>
            <a href="contact.html">Contact Us</a>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom-bar">
      <span class="footer-copy">© 2025 Hangzhou Hikstorage Technology Co., Ltd. All Rights Reserved.</span>
      <span class="footer-contact-info">Hangzhou, Zhejiang Province, China · 400-680-4998</span>
    </div>
    <img src="images/footer-decoration.png" alt="" class="footer-decoration" />
  </footer>"""

# ── 1. Append CSS to styles.css ───────────────────────────────────────────────
css_path = os.path.join(BASE, 'css', 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'OUTFIT FONT + UPDATED DESIGN TOKENS' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(NEW_CSS)
    print('Updated css/styles.css')
else:
    print('css/styles.css already updated')

# ── 2. Update each page ───────────────────────────────────────────────────────
pages = ['products', 'solutions', 'company', 'support', 'contact', 'where-to-buy', 'product-details']

for page in pages:
    path = os.path.join(BASE, f'{page}.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # Replace old navbar (any <nav class="navbar"> ... </nav> block)
    html = re.sub(
        r'<nav class="navbar">.*?</nav>',
        NEW_NAV,
        html,
        flags=re.DOTALL
    )

    # Replace old footer (site-footer or plain footer)
    html = re.sub(
        r'<footer class="site-footer">.*?</footer>',
        NEW_FOOTER,
        html,
        flags=re.DOTALL
    )
    # Also handle pages that already have class="footer"
    html = re.sub(
        r'<footer class="footer">.*?</footer>',
        NEW_FOOTER,
        html,
        flags=re.DOTALL
    )

    # Remove any leftover mobile-menu divs from old navbar
    html = re.sub(
        r'\s*<div class="mobile-menu"[^>]*>.*?</div>',
        '',
        html,
        flags=re.DOTALL
    )

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated {page}.html')
    else:
        print(f'No changes in {page}.html — check manually')
