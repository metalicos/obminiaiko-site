import AppKit
import WebKit

// Usage: websnap <url> <out.png> [width]
let args = CommandLine.arguments
let url = URL(string: args[1])!
let out = URL(fileURLWithPath: args[2])
let width = CGFloat(Double(args.count > 3 ? args[3] : "393") ?? 393)

final class Delegate: NSObject, WKNavigationDelegate {
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            webView.evaluateJavaScript("document.documentElement.scrollHeight") { value, _ in
                let full = CGFloat((value as? Double) ?? 2000); let height = args.count > 4 ? min(full, CGFloat(Double(args[4]) ?? 800)) : full
                webView.setFrameSize(NSSize(width: width, height: height))
                DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
                    let config = WKSnapshotConfiguration()
                    config.rect = CGRect(x: 0, y: 0, width: width, height: height)
                    webView.takeSnapshot(with: config) { image, error in
                        guard let image, let tiff = image.tiffRepresentation,
                              let rep = NSBitmapImageRep(data: tiff),
                              let png = rep.representation(using: .png, properties: [:]) else {
                            print("snapshot failed", error as Any); exit(1)
                        }
                        try? png.write(to: out)
                        print("ok \(Int(width))x\(Int(height))")
                        exit(0)
                    }
                }
            }
        }
    }
}

let app = NSApplication.shared
let config = WKWebViewConfiguration()
let web = WKWebView(frame: NSRect(x: 0, y: 0, width: width, height: 800), configuration: config)
web.customUserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 27_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0 Mobile/15E148 Safari/604.1"
let delegate = Delegate()
web.navigationDelegate = delegate
let window = NSWindow(contentRect: web.frame, styleMask: [.borderless], backing: .buffered, defer: false)
window.contentView = web
web.load(URLRequest(url: url, cachePolicy: .reloadIgnoringLocalCacheData))
app.run()
