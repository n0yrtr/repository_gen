package ${repository_impl_package};

import ${repository_package}.${name}Repository;
import ${dao_package}.${name}${dao_class_suffix};
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Repository;

@Repository
public class ${name}RepositoryImpl implements ${name}Repository {

    private ${name}${dao_class_suffix} ${lower_camel_name}${dao_class_suffix};
    private ModelMapper modelMapper;

    public ${name}RepositoryImpl(${name}${dao_class_suffix} ${lower_camel_name}${dao_class_suffix}, ModelMapper modelMapper) {
        this.${lower_camel_name}${dao_class_suffix} = ${lower_camel_name}${dao_class_suffix};
        this.modelMapper = modelMapper;
    }
}
