from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    targets = ["anthropic.com", "claude.ai", "stripe.com"]

    if any(target in flow.request.pretty_host for target in targets):
        nigeria_ip = "102.89.1.5"
        flow.request.headers["X-Forwarded-For"] = nigeria_ip
        flow.request.headers["CF-IPCountry"] = "NG"
        flow.request.headers["User-Agent"] = "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
        print(f"[OK] INJECTED NG IDENTITY -> {flow.request.pretty_host}")