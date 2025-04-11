@router.get("/oauth/microsoft/callback")
async def microsoft_callback(request: Request, code: str = Query(...)):
    try:
        # ...existing OAuth callback code...
        
        # After successful login and getting the token, add this:
        html_content = f"""
        <html>
        <body>
            <script>
                if (window.opener) {{
                    window.opener.postMessage({{ token: "{token}" }}, window.location.origin);
                    window.close();
                }}
            </script>
        </body>
        </html>
        """
        return HTMLResponse(content=html_content)