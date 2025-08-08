const { Convert, Validator } = require('@fhir-uck/fhir-converter-core');

const config = 'example_config'; // 替換為您的設定檔名稱
const data = [/* 您的範例資料 */];

async function exampleConvert() {
  const convert = new Convert(config);
  const result = await convert.convert(data);
  
  /*const validator = new Validator();*/
  /*const validationResult = await validator.validate(result);*/
  
  console.log('轉換結果:', result);
  /*console.log('驗證結果:', validationResult);*/
}

exampleConvert();