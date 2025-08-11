const { Convert, Validator } = require('@fhir-uck/fhir-converter-core');
const fs = require('fs');
const path = require('path');

const config = 'my_config'; // 替換為您的設定檔名稱
const data = require('./data.json');

async function exampleConvert() {
  const convert = new Convert(config);
  const result = await convert.convert(data);

  // 將結果寫入 JSON 檔案
  const outputPath = path.join(__dirname, 'conversion_results.json');
  fs.writeFileSync(outputPath, JSON.stringify(result, null, 2), 'utf8');
  console.log('轉換結果已匯出至:', outputPath);

  /*const validator = new Validator();*/
  /*const validationResult = await validator.validate(result);*/
  /*console.log('驗證結果:', validationResult);*/
}

exampleConvert();