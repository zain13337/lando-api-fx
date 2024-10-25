from unittest.mock import patch
import requests
import rs_parsepatch
    BugReferencesCheck,
    DiffAssessor,
    PatchCollectionAssessor,
from landoapi.repos import get_repos_for_env
GIT_PATCH_UTF8 = """
diff --git a/testing/web-platform/tests/html/dom/elements/global-attributes/dir-auto-dynamic-simple-textContent.html b/testing/web-platform/tests/html/dom/elements/global-attributes/dir-auto-dynamic-simple-textContent.html
new file mode 100644
--- /dev/null
+++ b/testing/web-platform/tests/html/dom/elements/global-attributes/dir-auto-dynamic-simple-textContent.html
@@ -0,0 +1,31 @@
+<!DOCTYPE html>
+<html class="reftest-wait">
+<meta charset="utf-8">
+<title>Dynamic changes with textContent and dir=auto</title>
+<link rel="match" href="dir-auto-dynamic-simple-ref.html">
+<div>Test for elements with dir="auto" whose content changes between directional and neutral</div>
+<div dir="auto" id="from_ltr_to_ltr">abc</div>
+<div dir="auto" id="from_ltr_to_rtl">abc</div>
+<div dir="auto" id="from_ltr_to_neutral">abc</div>
+<div dir="auto" id="from_rtl_to_ltr">אבג</div>
+<div dir="auto" id="from_rtl_to_rtl">אבג</div>
+<div dir="auto" id="from_rtl_to_neutral">אבג</div>
+<div dir="auto" id="from_neutral_to_ltr">123</div>
+<div dir="auto" id="from_neutral_to_rtl">123</div>
+<div dir="auto" id="from_neutral_to_neutral">123</div>
+<script>
+function changeContent() {
+  var directionalTexts = {ltr:"xyz", rtl:"ابج", neutral:"456"};
+
+  for (var dirFrom in directionalTexts) {
+    for (var dirTo in directionalTexts) {
+      var element = document.getElementById("from_" + dirFrom +
+                                            "_to_" + dirTo);
+      element.textContent = directionalTexts[dirTo];
+    }
+  }
+  document.documentElement.removeAttribute("class");
+}
+
+document.addEventListener("TestRendered", changeContent);
+</script>
""".strip()

GIT_FORMATPATCH_UTF8 = f"""
From 71ce7889eaa24616632a455636598d8f5c60b765 Mon Sep 17 00:00:00 2001
From: Connor Sheehan <sheehan@mozilla.com>
Date: Wed, 21 Feb 2024 10:20:49 +0000
Subject: [PATCH] Bug 1874040 - Move 1103348-1.html to WPT, and expand it.
 r=smaug

---
 .../dir-auto-dynamic-simple-textContent.html  | 31 ++++++++++++++++
 1 files changed, 31 insertions(+), 0 deletions(-)
 create mode 100644 testing/web-platform/tests/html/dom/elements/global-attributes/dir-auto-dynamic-simple-textContent.html
{GIT_PATCH_UTF8}
--
2.46.1
""".strip()

GIT_DIFF_FILENAME_TEMPLATE = """
diff --git a/{filename} b/{filename}
--- a/{filename}
+++ b/{filename}
@@ -12,5 +12,6 @@
 int main(int argc, char **argv)
 {{
        printf("hello, world!\n");
+       printf("sure am glad I'm using Mercurial!\n");
        return 0;
 }}
""".lstrip()
