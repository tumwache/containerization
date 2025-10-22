### How to create a container sample

#### 1. Clone project
git clone https://github.com/tumwache/containerization.git

#### 2. Go to scrap-records
cd user/containerization/scrap-records/

#### 3. Build the image (tagged name with py-scraper)
podman build -t py-scraper .

> To rebuild your image use (to clear the cache):   
podman build --no-cache -t py-scraper .

#### 4. Create scrapped data /output folder
mkdir output

#### 4. Run the image
podman run --rm -v "$(pwd)/output:/app/output" py-scraper


