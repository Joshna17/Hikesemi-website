(function () {
  'use strict';

  // ── Search data ──────────────────────────────────────────────────────────────
  var DATA = [
    // Products
    { type: 'product', icon: '💾', name: 'FUTURE CORE',          sub: 'SSD · PCIe 5.0 NVMe',     url: 'product-details.html', tags: ['ssd','nvme','pcie 5','pcie5','gen5','m.2','14000','fast','flagship','future core'] },
    { type: 'product', icon: '💾', name: 'FUTURE PRO',           sub: 'SSD · PCIe 4.0 NVMe',     url: 'products.html',        tags: ['ssd','nvme','pcie 4','pcie4','gen4','m.2','future pro','gaming'] },
    { type: 'product', icon: '💾', name: 'FUTURE',               sub: 'SSD · PCIe 4.0 NVMe',     url: 'products.html',        tags: ['ssd','nvme','pcie 4','m.2','value'] },
    { type: 'product', icon: '💾', name: 'FUTURE ECO',           sub: 'SSD · PCIe 3.0 NVMe',     url: 'products.html',        tags: ['ssd','nvme','pcie 3','m.2','budget','eco','future eco'] },
    { type: 'product', icon: '💿', name: 'WAVE(S) SATA',         sub: 'SSD · SATA III 2.5"',     url: 'products.html',        tags: ['ssd','sata','sata iii','2.5','wave','laptop','desktop'] },
    { type: 'product', icon: '🔧', name: 'D300 Pro Enterprise',  sub: 'SSD · Enterprise PCIe',   url: 'products.html',        tags: ['enterprise','server','d300','datacenter','endurance','pcie'] },
    { type: 'product', icon: '🧠', name: 'DDR5 RAM',             sub: 'Memory · DDR5',           url: 'products.html',        tags: ['ddr5','ram','memory','dimm','intel','amd','gaming'] },
    { type: 'product', icon: '🧠', name: 'DDR4 RAM',             sub: 'Memory · DDR4',           url: 'products.html',        tags: ['ddr4','ram','memory','dimm','sodimm','laptop','desktop'] },
    { type: 'product', icon: '📷', name: 'microSD Card',         sub: 'Memory Card · UHS-I/II',  url: 'products.html',        tags: ['microsd','sd card','memory card','camera','drone','dashcam','uhs'] },
    { type: 'product', icon: '💼', name: 'Portable SSD',         sub: 'External · USB 3.2',      url: 'products.html',        tags: ['portable','external','usb','usb 3.2','compact','backup','mobile'] },
    { type: 'product', icon: '🏠', name: 'Home NAS Drive',       sub: 'NAS · Network Storage',   url: 'products.html',        tags: ['nas','network','home','media','cloud','server','storage'] },
    { type: 'product', icon: '⚙️', name: 'Embedded Storage',     sub: 'Embedded · eMMC / UFS',   url: 'products.html',        tags: ['embedded','emmc','ufs','iot','industrial','module','flash'] },
    // Pages
    { type: 'page', icon: '🏠', name: 'Homepage',                sub: 'Home',           url: 'index.html',           tags: ['home','hiksemi','overview','main'] },
    { type: 'page', icon: '💾', name: 'All Products',            sub: 'Products',       url: 'products.html',        tags: ['products','all','catalog','browse'] },
    { type: 'page', icon: '🔬', name: 'FUTURE CORE Specs',       sub: 'Products',       url: 'product-details.html', tags: ['future core','specs','benchmark','pcie 5','details','nvme','datasheet'] },
    { type: 'page', icon: '🎮', name: 'Gaming Storage',          sub: 'Solutions',      url: 'solutions.html',       tags: ['gaming','ps5','xbox','pc','fps','load time','game'] },
    { type: 'page', icon: '🎬', name: 'Content Creation',        sub: 'Solutions',      url: 'solutions.html',       tags: ['content creation','video editing','4k','8k','creative','photographer','filmmaker'] },
    { type: 'page', icon: '📡', name: 'Surveillance Storage',    sub: 'Solutions',      url: 'solutions.html',       tags: ['surveillance','cctv','nvr','security camera','ip camera','24/7'] },
    { type: 'page', icon: '🏭', name: 'Industrial Storage',      sub: 'Solutions',      url: 'solutions.html',       tags: ['industrial','rugged','wide temperature','vibration','iot','embedded'] },
    { type: 'page', icon: '🏢', name: 'Enterprise & Datacenter', sub: 'Solutions',      url: 'solutions.html',       tags: ['enterprise','datacenter','server','qos','cloud','endurance'] },
    { type: 'page', icon: '💾', name: 'NAS & Backup',            sub: 'Solutions',      url: 'solutions.html',       tags: ['nas','backup','home','synology','qnap','media'] },
    { type: 'page', icon: '🏛️', name: 'About HIKSEMI',           sub: 'Company',        url: 'company.html',         tags: ['about','company','history','mission','hangzhou','who we are'] },
    { type: 'page', icon: '🛠️', name: 'Support Center',          sub: 'Support',        url: 'support.html',         tags: ['support','help','warranty','rma','firmware','faq','download','compatibility'] },
    { type: 'page', icon: '⚡', name: 'Warranty & RMA',          sub: 'Support',        url: 'support.html',         tags: ['warranty','rma','repair','replacement','claim','return'] },
    { type: 'page', icon: '📰', name: 'News & Press',            sub: 'News',           url: 'news.html',            tags: ['news','press','launch','award','announcement','media','blog'] },
    { type: 'page', icon: '📍', name: 'Where to Buy',            sub: 'Partners',       url: 'where-to-buy.html',    tags: ['buy','store','reseller','dealer','retail','amazon','distributor'] },
    { type: 'page', icon: '🤝', name: 'Become a Dealer',         sub: 'Partners',       url: 'become-a-dealer.html', tags: ['dealer','partner','distributor','reseller','apply','join','business'] },
    { type: 'page', icon: '✉️', name: 'Contact HIKSEMI',         sub: 'Contact',        url: 'contact.html',         tags: ['contact','email','phone','sales','support','press','headquarters'] },
  ];

  var POPULAR = ['PCIe 5.0', 'DDR5', 'NVMe SSD', 'Gaming', 'Warranty', 'Enterprise', 'Surveillance'];

  var QUICK = DATA.filter(function(d) {
    return ['All Products','Support Center','Where to Buy','Contact HIKSEMI','About HIKSEMI'].indexOf(d.name) !== -1;
  });

  // ── Overlay markup ───────────────────────────────────────────────────────────
  var OVERLAY_HTML = [
    '<div class="srch-ov" id="srchOv" role="dialog" aria-modal="true" aria-label="Site Search">',
    '  <div class="srch-ov-backdrop" id="srchOvBd"></div>',
    '  <div class="srch-ov-panel">',
    '    <div class="srch-ov-top">',
    '      <span class="srch-ov-icon">',
    '        <svg width="18" height="18" viewBox="0 0 18 18" fill="none">',
    '          <circle cx="8" cy="8" r="5.5" stroke="currentColor" stroke-width="1.5"/>',
    '          <path d="M12.5 12.5L16 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    '        </svg>',
    '      </span>',
    '      <input class="srch-ov-field" id="srchOvField" type="search" placeholder="Search products, solutions, support…" autocomplete="off" spellcheck="false" />',
    '      <button class="srch-ov-esc" id="srchOvClose" aria-label="Close search">ESC</button>',
    '    </div>',
    '    <div class="srch-ov-body" id="srchOvBody"></div>',
    '    <div class="srch-ov-footer">',
    '      <span class="srch-ov-hint"><kbd>↑↓</kbd> navigate &nbsp;·&nbsp; <kbd>↵</kbd> open &nbsp;·&nbsp; <kbd>ESC</kbd> close</span>',
    '      <span class="srch-ov-count" id="srchOvCount"></span>',
    '    </div>',
    '  </div>',
    '</div>'
  ].join('\n');

  // ── Utilities ────────────────────────────────────────────────────────────────
  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function matches(item, q) {
    var hay = [item.name, item.sub].concat(item.tags || []).join(' ').toLowerCase();
    return q.split(/\s+/).every(function(w) { return !w || hay.indexOf(w) !== -1; });
  }

  // ── Render helpers ───────────────────────────────────────────────────────────
  function renderDefault() {
    var tags = POPULAR.map(function(t) {
      return '<button class="srch-ov-tag" data-query="' + esc(t) + '">' + esc(t) + '</button>';
    }).join('');

    var links = QUICK.map(function(item) {
      return '<a class="srch-ov-row" href="' + esc(item.url) + '">' +
        '<div class="srch-ov-row-icon">' + item.icon + '</div>' +
        '<div class="srch-ov-row-body">' +
          '<span class="srch-ov-row-title">' + esc(item.name) + '</span>' +
          '<span class="srch-ov-row-sub">' + esc(item.sub) + '</span>' +
        '</div>' +
        '<span class="srch-ov-row-badge">' + esc(item.sub) + '</span>' +
      '</a>';
    }).join('');

    return '<div class="srch-ov-section">' +
        '<div class="srch-ov-section-label">Popular searches</div>' +
        '<div class="srch-ov-tags">' + tags + '</div>' +
      '</div>' +
      '<div class="srch-ov-divider"></div>' +
      '<div class="srch-ov-section"><div class="srch-ov-section-label">Quick links</div></div>' +
      links;
  }

  function renderResults(results, rawQ) {
    if (!results.length) {
      return '<div class="srch-ov-empty">' +
        '<div class="srch-ov-empty-icon">🔍</div>' +
        '<div class="srch-ov-empty-title">No results for “' + esc(rawQ) + '”</div>' +
        '<div class="srch-ov-empty-sub">Try different keywords or browse our products.</div>' +
      '</div>';
    }
    return results.map(function(item, i) {
      return '<a class="srch-ov-row" href="' + esc(item.url) + '" data-idx="' + i + '">' +
        '<div class="srch-ov-row-icon">' + item.icon + '</div>' +
        '<div class="srch-ov-row-body">' +
          '<span class="srch-ov-row-title">' + esc(item.name) + '</span>' +
          '<span class="srch-ov-row-sub">' + esc(item.sub) + '</span>' +
        '</div>' +
        '<span class="srch-ov-row-badge ' + item.type + '">' +
          (item.type === 'product' ? 'Product' : esc(item.sub)) +
        '</span>' +
      '</a>';
    }).join('');
  }

  // ── State ────────────────────────────────────────────────────────────────────
  var overlay, field, body, countEl, focusedIdx;

  function attachTagListeners() {
    var tags = body.querySelectorAll('.srch-ov-tag');
    for (var i = 0; i < tags.length; i++) {
      (function(btn) {
        btn.addEventListener('click', function() {
          field.value = btn.getAttribute('data-query');
          onInput();
          field.focus();
        });
      })(tags[i]);
    }
  }

  function focusRow(idx) {
    var rows = body.querySelectorAll('.srch-ov-row');
    for (var i = 0; i < rows.length; i++) rows[i].classList.remove('focused');
    if (idx >= 0 && idx < rows.length) {
      rows[idx].classList.add('focused');
      rows[idx].scrollIntoView({ block: 'nearest' });
    }
    focusedIdx = idx;
  }

  function onInput() {
    var raw = field.value.trim();
    var q   = raw.toLowerCase();
    focusedIdx = -1;

    if (q.length < 2) {
      body.innerHTML = renderDefault();
      countEl.textContent = '';
      attachTagListeners();
      return;
    }

    var results = DATA.filter(function(item) { return matches(item, q); });
    body.innerHTML = renderResults(results, raw);
    countEl.textContent = results.length ? results.length + ' result' + (results.length !== 1 ? 's' : '') : '';
  }

  function open() {
    overlay.classList.add('open');
    document.body.classList.add('srch-open');
    field.value = '';
    focusedIdx = -1;
    body.innerHTML = renderDefault();
    countEl.textContent = '';
    attachTagListeners();
    setTimeout(function() { field.focus(); }, 40);
  }

  function close() {
    overlay.classList.remove('open');
    document.body.classList.remove('srch-open');
  }

  function onKeyDown(e) {
    var isOpen = overlay.classList.contains('open');

    // Cmd/Ctrl+K global toggle
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      isOpen ? close() : open();
      return;
    }

    if (!isOpen) return;

    var rows = body.querySelectorAll('.srch-ov-row');
    if (e.key === 'Escape') {
      close();
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      focusRow(Math.min(focusedIdx + 1, rows.length - 1));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      var next = focusedIdx - 1;
      if (next < 0) {
        focusRow(-1);
        field.focus();
      } else {
        focusRow(next);
      }
    } else if (e.key === 'Enter' && focusedIdx >= 0 && rows[focusedIdx]) {
      e.preventDefault();
      rows[focusedIdx].click();
    }
  }

  // ── Init ─────────────────────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function() {
    // Inject overlay into page
    document.body.insertAdjacentHTML('beforeend', OVERLAY_HTML);

    overlay  = document.getElementById('srchOv');
    field    = document.getElementById('srchOvField');
    body     = document.getElementById('srchOvBody');
    countEl  = document.getElementById('srchOvCount');

    // Wire all search buttons — intercept navigation if they link to search.html
    var btns = document.querySelectorAll('.nav-search-btn');
    for (var i = 0; i < btns.length; i++) {
      btns[i].addEventListener('click', function(e) {
        e.preventDefault();
        open();
      });
    }

    document.getElementById('srchOvClose').addEventListener('click', close);
    document.getElementById('srchOvBd').addEventListener('click', close);
    field.addEventListener('input', onInput);
    document.addEventListener('keydown', onKeyDown);
  });
})();
