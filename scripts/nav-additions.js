/* The page table of contents and the subpage footer used to live in a
   vendored copy of mdBook's index.hbs. They are created here instead so the
   wiki runs on the stock theme and mdBook upgrades need no template merge. */
(function () {
	var main = document.querySelector("#content > main");
	if (main && !document.querySelector(".sidetoc")) {
		var sidetoc = document.createElement("div");
		sidetoc.className = "sidetoc";
		var nav = document.createElement("nav");
		nav.className = "pagetoc";
		sidetoc.appendChild(nav);
		main.insertBefore(sidetoc, main.firstChild);
	}
	if (main && !document.getElementById("subpage-footer")) {
		var footer = document.createElement("footer");
		footer.id = "subpage-footer";
		var label = document.createElement("p");
		label.textContent = "Subpages";
		footer.appendChild(label);
		main.parentElement.appendChild(footer);
	}
})();

// Un-active everything when you click it
var pagetocElement = document.getElementsByClassName("pagetoc")[0];
if (pagetocElement && pagetocElement.children) {
	Array.prototype.forEach.call(pagetocElement.children, (el) => {
		el.addEventListener("click", () => {
			Array.prototype.forEach.call(pagetocElement.children, (el) => {
				el.classList.remove("active");
			});
			el.classList.add("active");
		});
	});
}

var updateFunction = () => {
	var id;
	var elements = document.getElementsByClassName("header");
	Array.prototype.forEach.call(elements, (el) => {
		if (el.href && window.pageYOffset >= el.offsetTop) {
			id = el;
		}
	});

	var pagetocElement = document.getElementsByClassName("pagetoc")[0];
	if (!pagetocElement || !pagetocElement.children) return;

	Array.prototype.forEach.call(pagetocElement.children, (el) => {
		el.classList.remove("active");
	});

	if (id == undefined) return;

	Array.prototype.forEach.call(pagetocElement.children, (el) => {
		if (id.href.localeCompare(el.href) == 0) {
			el.classList.add("active");
		}
	});
};

window.addEventListener("load", () => {
	/* Scroll the page index on the left to the current active page */
	var active = document.querySelector(".chapter li a.active");
	if (active) {
		active.scrollIntoView({
			behavior: "auto",
			block: "center",
			inline: "nearest",
		});
	}

	/* A visible way into search, at the top of the sidebar. Added on load
	   because the sidebar fills itself in after this script first runs. */
	var scrollbox = document.querySelector("#sidebar .sidebar-scrollbox");
	var toggle = document.getElementById("search-toggle");
	if (scrollbox && toggle && !document.querySelector(".wiki-sidebar-search")) {
		var search = document.createElement("button");
		search.type = "button";
		search.className = "wiki-sidebar-search";
		search.textContent = "Search the wiki";
		var hint = document.createElement("kbd");
		hint.textContent = "S";
		search.appendChild(hint);
		search.addEventListener("click", () => {
			var wrapper = document.getElementById("search-wrapper");
			if (wrapper && wrapper.classList.contains("hidden")) toggle.click();
			var bar = document.getElementById("searchbar");
			if (bar) bar.focus();
		});
		scrollbox.insertBefore(search, scrollbox.firstChild);
	}

	/* Trail ("you are here") above the page, and the footer list below it.
	   Both are read from the sidebar, so they follow SUMMARY.md and cannot
	   go stale. A page with subpages lists them; any other page lists the
	   rest of its section. */
	var main = document.querySelector("#content > main");
	var home = document.querySelector(".chapter > li.chapter-item > a");
	var parentOf = (link) => {
		var list = link.closest("ol.section");
		var holder = list ? list.parentElement.previousElementSibling : null;
		return holder ? holder.querySelector(":scope > a:not(.toggle), :scope > div") : null;
	};
	var plainLink = (source) => {
		var item;
		if (source.href) {
			item = document.createElement("a");
			item.href = source.href;
		} else {
			item = document.createElement("span");
		}
		item.textContent = source.textContent.trim();
		return item;
	};
	if (active && main && home && active !== home && !document.querySelector(".wiki-trail")) {
		var chain = [];
		for (var step = parentOf(active); step; step = step.tagName === "A" ? parentOf(step) : parentOf(step.parentElement)) {
			chain.unshift(step);
		}
		chain.unshift(home);
		var trail = document.createElement("nav");
		trail.className = "wiki-trail";
		trail.setAttribute("aria-label", "You are here");
		chain.forEach((source) => {
			trail.appendChild(plainLink(source));
			var divider = document.createElement("span");
			divider.className = "wiki-trail-divider";
			divider.setAttribute("aria-hidden", "true");
			divider.textContent = "\u203A";
			trail.appendChild(divider);
		});
		var here = document.createElement("span");
		here.setAttribute("aria-current", "page");
		here.textContent = active.textContent.trim();
		trail.appendChild(here);
		var sidetoc = main.querySelector(":scope > .sidetoc");
		main.insertBefore(trail, sidetoc ? sidetoc.nextSibling : main.firstChild);
	}

	var nextListEl = active ? active.parentElement.nextElementSibling : null;
	var footer = document.getElementById("subpage-footer");
	if (footer) {
		footer.style.display = "none";
		var subpages = nextListEl ? nextListEl.querySelector(":scope > .section") : null;
		var siblings = active ? active.closest("ol.section") : null;
		var section = active ? parentOf(active) : null;
		var fill = (label, list) => {
			var copy = list.cloneNode(true);
			/* One level is enough: drop nested lists and their toggles. */
			copy.querySelectorAll("ol.section, a.toggle").forEach((el) => {
				var holder = el.tagName === "OL" ? el.parentElement : el;
				holder.remove();
			});
			copy.querySelectorAll("a.active").forEach((el) => {
				el.setAttribute("aria-current", "page");
			});
			footer.querySelector("p").textContent = label;
			footer.appendChild(copy);
			footer.style.display = "block";
		};
		/* A section page that already describes each of its pages needs no second list. */
		var described = (list) => {
			var onPage = Array.prototype.map.call(main ? main.querySelectorAll("a[href]") : [], (el) => el.href);
			return Array.prototype.every.call(list.querySelectorAll(":scope > li > a:not(.toggle)"), (el) => onPage.indexOf(el.href) !== -1);
		};
		if (subpages && described(subpages)) {
			/* nothing to add */
		} else if (subpages) {
			fill("In this section", subpages);
		} else if (siblings && section && siblings.querySelectorAll(":scope > li > a:not(.toggle)").length > 1) {
			fill("More in " + section.textContent.trim(), siblings);
		}
	}

	/* Populate pagetoc sidebar */

	var pagetoc = document.getElementsByClassName("pagetoc")[0];
	if (!pagetoc) return;

	var elements = document.getElementsByClassName("header");
	// don't show pagetoc sidebar with less than 2 headers
	if (elements.length < 2) return;

	Array.prototype.forEach.call(elements, (el) => {
		try {
			var link = document.createElement("a");

			// Indent shows hierarchy
			var indent = "";
			if (el.parentElement && el.parentElement.tagName) {
				switch (el.parentElement.tagName) {
					case "H2":
						indent = "20px";
						break;
					case "H3":
						indent = "40px";
						break;
					case "H4":
						indent = "60px";
						break;
					case "H5":
						indent = "80px";
						break;
					default:
						break;
				}
			}

			if (el.text !== undefined && el.href !== undefined) {
				link.appendChild(document.createTextNode(el.text));
				link.style.paddingLeft = indent;
				link.href = el.href;
				if (pagetoc) {
					pagetoc.appendChild(link);
				}
			}
		} catch (e) {
			console.warn("Error creating pagetoc link:", e);
		}
	});
	updateFunction.call();
});

// Handle active elements on scroll
window.addEventListener("scroll", updateFunction);
