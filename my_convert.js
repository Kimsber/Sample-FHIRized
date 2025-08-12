const { Convert, Validator } = require('@fhir-uck/fhir-converter-core');
const fs = require('fs');
const path = require('path');

const config = 'my_config'; // 替換為您的設定檔名稱
const data = require('./data.json');

async function exampleConvert() {
  const convert = new Convert(config);
  const result = await convert.convert(data);

  let output = { bundle: result };

  // If validate is true in config, run validation and include in output
  if (config.validate) {
    const validator = new Validator();
    const validationResults = await validator.validate(result);
    output.validationResults = validationResults;
  }

  // Write conversion result (with or without validation)
  const outputPath = path.join(__dirname, 'conversion_results.json');
  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2), 'utf8');
  console.log('轉換結果已匯出至:', outputPath);
}

exampleConvert();