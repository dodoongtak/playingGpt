import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

async def extract_text(page, selector="main"):
    """Extract text content from a page."""
    try:
        content = await page.inner_text(selector)
        return content.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

async def main():
    # URLs specifically targeting the information needed for the challenge questions
    urls = [
        # AI Gateway overview and capabilities
        "https://developers.cloudflare.com/ai-gateway/",
        
        # Workers AI models and pricing
        "https://developers.cloudflare.com/workers-ai/models/",
        "https://developers.cloudflare.com/workers-ai/",  # Main Workers AI page might have pricing
        
        # Vectorize documentation
        "https://developers.cloudflare.com/vectorize/",
        "https://developers.cloudflare.com/vectorize/get-started/",  # Might have limits info
        "https://developers.cloudflare.com/vectorize/configuration/",  # Might have limits info
    ]
    
    all_content = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for url in urls:
            print(f"Crawling: {url}")
            try:
                await page.goto(url, wait_until="networkidle")
                content = await extract_text(page)
                
                if content:
                    # Add section header for context
                    section_header = f"\n\n=== Content from {url} ===\n\n"
                    all_content.append(section_header + content)
                    print(f"Successfully extracted content from {url}")
                else:
                    print(f"No content found at {url}")
                
            except Exception as e:
                print(f"Error crawling {url}: {e}")
        
        await browser.close()
    
    # Save all content to document.txt
    output_path = Path("document.txt")
    output_path.write_text("\n".join(all_content), encoding="utf-8")
    print(f"\nDocumentation saved to {output_path.absolute()}")
    
    # Print verification message
    print("\nVerification:")
    print("1. AI Gateway capabilities should be in the content")
    print("2. Workers AI model pricing (including llama-2-7b-chat-fp16) should be in the content")
    print("3. Vectorize index limits should be in the content")

if __name__ == "__main__":
    asyncio.run(main()) 