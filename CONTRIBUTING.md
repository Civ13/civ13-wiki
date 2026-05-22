If you want to send a pull request to our project and the **GitHub web editor** is not enough, you can develop locally:

### Quick Start

1. Fork or clone this repository.

2. Clone it to your computer and navigate to the `civ13-wiki/` folder.

3. **Windows (No installation needed!):**
   ```powershell
   .\mdbook.exe serve
   ```
   The wiki will open at `http://localhost:3000` with live reloading.

   **macOS/Linux:**
   ```bash
   cargo install mdbook  # First time only
   mdbook serve
   ```

4. Make your changes in the `src/` folder and they'll automatically rebuild in your browser.

5. Push changes to your fork and create a Pull Request for us to review.

### Local Building

- **Build only:** `./mdbook.exe build` (outputs to `book/html/`)
- **Live development:** `./mdbook.exe serve` (runs local server with auto-reload)

For more detailed information, check [Contributing to the Wiki](src/Contributing_to_the_Wiki.md) in the wiki itself.